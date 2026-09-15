import math
from typing import List, Tuple
from src.data_models import (
    Service,
    Task,
    Evidence,
    RiskAssessment,
    TrustAssessment,
    DecisionRecommendation,
)


class TrustEvaluationEngine:
    """
    Multidimensional Trust Evaluation Engine.
    Implements the proposed formal model combining:
    Identity, Capability, Task-Specific History, Evidence Quality, Discounted Reputation, and Risk.
    """

    def __init__(
        self,
        sybil_reputation_discount_delta: float = 0.25,
        evidence_confidence_gamma: float = 0.35,
        epsilon: float = 1e-6
    ):
        self.delta = sybil_reputation_discount_delta
        self.gamma = evidence_confidence_gamma
        self.epsilon = epsilon

    def evaluate(
        self,
        candidate: Service,
        task: Task,
        weighted_evidence: List[Tuple[Evidence, float]],
        risk: RiskAssessment
    ) -> TrustAssessment:
        # 1. Identity & Reachability pre-check
        if not candidate.is_reachable:
            return TrustAssessment(
                candidate_id=candidate.agent_id,
                task_id=task.task_id,
                task_domain=task.domain,
                expected_success_rate=0.0,
                evidence_confidence_omega=0.0,
                evidence_records_evaluated=0,
                discounted_reputation=0.0,
                risk_threshold_required=risk.confidence_threshold,
                recommendation=DecisionRecommendation.REJECT,
                justification="Service endpoint is unreachable."
            )

        # 2. Compute Task-Specific Historical Performance (mu_history)
        total_weight = sum(w for _, w in weighted_evidence)
        if total_weight > 0.0:
            weighted_success = sum(
                w * (1.0 if rec.is_success else 0.0) * rec.rigor_score
                for rec, w in weighted_evidence
            )
            mu_history = weighted_success / (total_weight + self.epsilon)
        else:
            mu_history = 0.5  # Neutral prior if zero domain evidence

        # 3. Compute Evidence Volume Confidence (Omega)
        # Omega = 1 - e^(-gamma * sum(w))
        omega = 1.0 - math.exp(-self.gamma * total_weight)

        # 4. Compute Discounted Reputation
        discounted_rep = self.delta * candidate.raw_reputation_score

        # 5. Synthesized Expected Success: E = Omega * mu_history + (1 - Omega) * (delta * rho)
        expected_success = (omega * mu_history) + ((1.0 - omega) * discounted_rep)
        expected_success = max(0.0, min(1.0, expected_success))

        # 6. Gated Decision Recommendation
        if expected_success >= risk.confidence_threshold and omega >= risk.min_evidence_confidence:
            recommendation = DecisionRecommendation.ACCEPT
            justification = f"Meets confidence ({omega:.2f} >= {risk.min_evidence_confidence}) and expected success ({expected_success:.2f} >= {risk.confidence_threshold})."
        elif expected_success >= (risk.confidence_threshold * 0.8) and risk.risk_score <= 0.3:
            recommendation = DecisionRecommendation.FALLBACK_CAUTION
            justification = "Tolerable for low-stakes exploration despite low evidence volume."
        else:
            recommendation = DecisionRecommendation.REJECT
            justification = f"Fails risk gate: expected {expected_success:.2f} < threshold {risk.confidence_threshold} or omega {omega:.2f} < {risk.min_evidence_confidence}."

        return TrustAssessment(
            candidate_id=candidate.agent_id,
            task_id=task.task_id,
            task_domain=task.domain,
            expected_success_rate=round(expected_success, 4),
            evidence_confidence_omega=round(omega, 4),
            evidence_records_evaluated=len(weighted_evidence),
            discounted_reputation=round(discounted_rep, 4),
            risk_threshold_required=risk.confidence_threshold,
            recommendation=recommendation,
            justification=justification
        )
