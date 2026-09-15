import math
import time
from typing import List, Optional, Tuple
from src.data_models import Evidence, Task


class EvidenceRetriever:
    """
    RAG Evidence Retriever.
    Performs semantic vector similarity matching and exponential time-decay weighting
    over historical interaction records.
    """

    def __init__(
        self,
        relevance_threshold: float = 0.65,
        decay_half_life_seconds: float = 86400 * 30  # 30 days
    ):
        self.relevance_threshold = relevance_threshold
        # lambda = ln(2) / half_life
        self.decay_lambda = math.log(2) / decay_half_life_seconds

    def retrieve_weighted_evidence(
        self,
        candidate_id: str,
        task: Task,
        all_candidate_evidence: List[Evidence],
        current_time: Optional[int] = None
    ) -> List[Tuple[Evidence, float]]:
        """
        Retrieves evidence records matching candidate and domain,
        returning a list of (Evidence, weight) tuples.
        """
        now = current_time or int(time.time())
        weighted_records: List[Tuple[Evidence, float]] = []

        for record in all_candidate_evidence:
            if record.service_id != candidate_id:
                continue

            # 1. Semantic Domain Similarity
            sim = self._calculate_similarity(task, record)
            if sim < self.relevance_threshold:
                continue

            # 2. Exponential Time Decay: e^(-lambda * delta_t)
            delta_t = max(0, now - record.timestamp)
            time_weight = math.exp(-self.decay_lambda * delta_t)

            total_weight = sim * time_weight
            weighted_records.append((record, total_weight))

        return weighted_records

    def _calculate_similarity(self, task: Task, record: Evidence) -> float:
        """Computes semantic similarity between current task and historical record."""
        # Exact domain match provides high baseline
        if task.domain == record.task_domain:
            if task.embedding and record.task_embedding:
                return self._cosine_similarity(task.embedding, record.task_embedding)
            return 1.0

        # Different domain: check vector similarity if embeddings present
        if task.embedding and record.task_embedding:
            return self._cosine_similarity(task.embedding, record.task_embedding)

        # Disjoint domains without embeddings have zero relevance
        return 0.0

    @staticmethod
    def _cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))
        if norm1 <= 0.0 or norm2 <= 0.0:
            return 0.0
        return max(0.0, dot / (norm1 * norm2))
