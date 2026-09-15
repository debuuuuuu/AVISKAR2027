import random
import time
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from src.data_models import (
    Service,
    Task,
    SelectionDecision,
    DecisionRecommendation,
    Evidence,
)
from src.trust.evaluator import TrustEvaluationEngine
from src.trust.risk import RiskAssessmentLayer
from src.rag.retriever import EvidenceRetriever


class BaseSelectionStrategy(ABC):
    """Abstract interface for candidate service selection strategies."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def select(
        self,
        candidates: List[Service],
        task: Task,
        all_evidence: List[Evidence]
    ) -> SelectionDecision:
        pass


class RandomSelectionStrategy(BaseSelectionStrategy):
    """
    Strategy 1: Random Selection (Null Baseline).
    Selects uniformly at random from reachable candidates.
    """

    def __init__(self, seed: int = 42):
        super().__init__("RandomSelection")
        self.rng = random.Random(seed)

    def select(
        self,
        candidates: List[Service],
        task: Task,
        all_evidence: List[Evidence]
    ) -> SelectionDecision:
        start_time = time.perf_counter()
        reachable = [c for c in candidates if c.is_reachable]

        latency_ms = (time.perf_counter() - start_time) * 1000

        if not reachable:
            return SelectionDecision(
                task_id=task.task_id,
                strategy_used=self.name,
                selected_service_id=None,
                is_rejected=True,
                decision_latency_ms=latency_ms
            )

        chosen = self.rng.choice(reachable)
        return SelectionDecision(
            task_id=task.task_id,
            strategy_used=self.name,
            selected_service_id=chosen.agent_id,
            is_rejected=False,
            decision_latency_ms=latency_ms
        )


class ReputationOnlySelectionStrategy(BaseSelectionStrategy):
    """
    Strategy 2: Reputation-Only Selection (ERC-8004 Industry Baseline).
    Selects candidate with the highest raw global reputation score.
    """

    def __init__(self):
        super().__init__("ReputationOnlySelection")

    def select(
        self,
        candidates: List[Service],
        task: Task,
        all_evidence: List[Evidence]
    ) -> SelectionDecision:
        start_time = time.perf_counter()
        reachable = [c for c in candidates if c.is_reachable]

        latency_ms = (time.perf_counter() - start_time) * 1000

        if not reachable:
            return SelectionDecision(
                task_id=task.task_id,
                strategy_used=self.name,
                selected_service_id=None,
                is_rejected=True,
                decision_latency_ms=latency_ms
            )

        # Sort descending by raw public reputation score
        scores = {c.agent_id: c.raw_reputation_score for c in reachable}
        best_candidate = max(reachable, key=lambda c: c.raw_reputation_score)

        return SelectionDecision(
            task_id=task.task_id,
            strategy_used=self.name,
            selected_service_id=best_candidate.agent_id,
            is_rejected=False,
            trust_scores_evaluated=scores,
            decision_latency_ms=latency_ms
        )


class EvidenceBasedSelectionStrategy(BaseSelectionStrategy):
    """
    Strategy 3: Evidence-Based Selection (Proposed Framework).
    Retrieves task-specific evidence via RAG, evaluates multidimensional trust,
    enforces risk gating, and supports Safe Rejection.
    """

    def __init__(
        self,
        trust_engine: TrustEvaluationEngine,
        risk_layer: RiskAssessmentLayer,
        retriever: EvidenceRetriever
    ):
        super().__init__("EvidenceBasedSelection")
        self.trust_engine = trust_engine
        self.risk_layer = risk_layer
        self.retriever = retriever

    def select(
        self,
        candidates: List[Service],
        task: Task,
        all_evidence: List[Evidence]
    ) -> SelectionDecision:
        start_time = time.perf_counter()
        risk_assessment = self.risk_layer.assess(task)

        evaluated_scores: Dict[str, float] = {}
        qualified_candidates: List[tuple[Service, float]] = []

        for candidate in candidates:
            if not candidate.is_reachable:
                continue

            # 1. RAG: Retrieve task-specific weighted evidence
            weighted_evidence = self.retriever.retrieve_weighted_evidence(
                candidate_id=candidate.agent_id,
                task=task,
                all_candidate_evidence=all_evidence
            )

            # 2. Evaluate multidimensional trust
            assessment = self.trust_engine.evaluate(
                candidate=candidate,
                task=task,
                weighted_evidence=weighted_evidence,
                risk=risk_assessment
            )

            evaluated_scores[candidate.agent_id] = assessment.expected_success_rate

            # 3. Gating check
            if assessment.recommendation in [DecisionRecommendation.ACCEPT, DecisionRecommendation.FALLBACK_CAUTION]:
                qualified_candidates.append((candidate, assessment.expected_success_rate))

        latency_ms = (time.perf_counter() - start_time) * 1000

        # Safe Rejection: If no candidate qualifies
        if not qualified_candidates:
            return SelectionDecision(
                task_id=task.task_id,
                strategy_used=self.name,
                selected_service_id=None,
                is_rejected=True,
                trust_scores_evaluated=evaluated_scores,
                decision_latency_ms=latency_ms
            )

        # Select candidate with highest expected success
        best_candidate, _ = max(qualified_candidates, key=lambda x: x[1])
        return SelectionDecision(
            task_id=task.task_id,
            strategy_used=self.name,
            selected_service_id=best_candidate.agent_id,
            is_rejected=False,
            trust_scores_evaluated=evaluated_scores,
            decision_latency_ms=latency_ms
        )
