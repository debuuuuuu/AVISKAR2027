from typing import Any, Dict, List, Optional
from src.data_models import (
    Task,
    Service,
    Interaction,
    VerificationRecord,
    SelectionDecision,
    Evidence,
)
from src.services.base import BaseServiceAgent
from src.selection.strategies import BaseSelectionStrategy
from src.verification.verifier import ResultVerifier
from src.evidence.store import EvidenceStore
from src.blockchain.provenance import BlockchainProvenanceAnchor


class AutonomousClientAgent:
    """
    Autonomous Client Agent (Orchestrator).
    Coordinates candidate discovery, trust-based service selection,
    task dispatch, sandboxed result verification, and evidence anchoring.
    """

    def __init__(
        self,
        agent_id: str,
        selection_strategy: BaseSelectionStrategy,
        verifier: ResultVerifier,
        evidence_store: EvidenceStore,
        provenance_anchor: Optional[BlockchainProvenanceAnchor] = None
    ):
        self.agent_id = agent_id
        self.strategy = selection_strategy
        self.verifier = verifier
        self.evidence_store = evidence_store
        self.provenance_anchor = provenance_anchor or BlockchainProvenanceAnchor()

    def run_task(
        self,
        task: Task,
        candidate_services: List[Service],
        service_instances: Dict[str, BaseServiceAgent]
    ) -> Dict[str, Any]:
        """
        Executes the complete 8-step closed feedback loop:
        1. Select service candidate
        2. Dispatch execution
        3. Sandboxed verification
        4. Record evidence
        5. Return structured result
        """
        all_evidence = self.evidence_store.get_all_records()

        # Step 1: Selection Decision
        decision: SelectionDecision = self.strategy.select(
            candidates=candidate_services,
            task=task,
            all_evidence=all_evidence
        )

        if decision.is_rejected or not decision.selected_service_id:
            return {
                "task_id": task.task_id,
                "status": "REJECTED",
                "reason": "Safe Rejection triggered: No candidate met trust/risk threshold.",
                "decision": decision.model_dump(),
                "result": None,
                "is_success": False
            }

        # Step 2: Task Execution via Service
        service_id = decision.selected_service_id
        service_instance = service_instances.get(service_id)
        if not service_instance:
            return {
                "task_id": task.task_id,
                "status": "EXECUTION_ERROR",
                "reason": f"Service instance {service_id} not instantiated in testbed.",
                "decision": decision.model_dump(),
                "result": None,
                "is_success": False
            }

        interaction: Interaction = service_instance.execute(task)

        # Step 3: Sandboxed Result Verification
        verification: VerificationRecord = self.verifier.verify(task, interaction)

        # Step 4: Evidence Recording & Provenance Anchoring
        evidence: Evidence = self.evidence_store.record_interaction(
            task=task,
            interaction=interaction,
            verification=verification
        )

        # Step 5: Anchor state commitment if threshold reached
        if self.evidence_store.count() % 10 == 0:
            hashes = [e.provenance_hash for e in self.evidence_store.get_all_records()]
            self.provenance_anchor.commit_batch(hashes)

        return {
            "task_id": task.task_id,
            "status": "COMPLETED",
            "selected_service_id": service_id,
            "decision": decision.model_dump(),
            "interaction": interaction.model_dump(),
            "verification": verification.model_dump(),
            "evidence_id": evidence.evidence_id,
            "is_success": verification.is_success
        }
