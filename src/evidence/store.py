import time
from typing import Dict, List, Optional
from src.data_models import Evidence, VerificationRecord, Interaction, Task


class EvidenceStore:
    """
    Evidence Store.
    Maintains local, queryable historical interaction and verification records.
    """

    def __init__(self):
        # In-memory storage indexed by service_id
        self._records_by_service: Dict[str, List[Evidence]] = {}
        self._all_records: List[Evidence] = []

    def record_interaction(
        self,
        task: Task,
        interaction: Interaction,
        verification: VerificationRecord
    ) -> Evidence:
        """Constructs an Evidence record and appends it to the store."""
        evidence = Evidence(
            task_id=task.task_id,
            service_id=interaction.service_id,
            task_domain=task.domain,
            task_embedding=task.embedding,
            risk_level=task.risk_level,
            latency_ms=interaction.latency_ms,
            is_success=verification.is_success,
            rigor_score=verification.rigor_score,
            verification_mode=verification.verification_mode,
            provenance_hash=verification.provenance_hash,
            timestamp=verification.timestamp
        )

        if interaction.service_id not in self._records_by_service:
            self._records_by_service[interaction.service_id] = []

        self._records_by_service[interaction.service_id].append(evidence)
        self._all_records.append(evidence)
        return evidence

    def get_evidence_for_service(
        self,
        service_id: str,
        domain: Optional[str] = None
    ) -> List[Evidence]:
        """Returns evidence records for a specific service, optionally filtered by domain."""
        records = self._records_by_service.get(service_id, [])
        if domain:
            records = [r for r in records if r.task_domain == domain]
        return records

    def get_all_records(self) -> List[Evidence]:
        return list(self._all_records)

    def count(self) -> int:
        return len(self._all_records)
