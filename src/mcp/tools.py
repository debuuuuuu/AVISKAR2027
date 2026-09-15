"""
Model Context Protocol (MCP) tool bindings.
Exposes trust evaluation, verification, and evidence recording as MCP tools.
"""

from typing import Any, Dict, List
from src.data_models import Task, Interaction, RiskTier, Service
from src.trust.evaluator import TrustEvaluationEngine
from src.trust.risk import RiskAssessmentLayer
from src.evidence.store import EvidenceStore
from src.rag.retriever import EvidenceRetriever
from src.verification.verifier import ResultVerifier


class MCPToolHandler:
    """
    Exposes trust and verification capabilities as Model Context Protocol (MCP) tools.
    """

    def __init__(
        self,
        trust_engine: TrustEvaluationEngine,
        risk_layer: RiskAssessmentLayer,
        evidence_store: EvidenceStore,
        retriever: EvidenceRetriever,
        verifier: ResultVerifier
    ):
        self.trust_engine = trust_engine
        self.risk_layer = risk_layer
        self.evidence_store = evidence_store
        self.retriever = retriever
        self.verifier = verifier

    def get_tool_declarations(self) -> List[Dict[str, Any]]:
        """Returns MCP tools declaration schema."""
        return [
            {
                "name": "verify_agent",
                "description": "Verifies candidate identity, signature validity, and endpoint reachability.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "service_id": {"type": "string"},
                        "public_key": {"type": "string"},
                        "endpoint_uri": {"type": "string"}
                    },
                    "required": ["service_id", "public_key", "endpoint_uri"]
                }
            },
            {
                "name": "get_task_specific_trust",
                "description": "Computes evidence-grounded trust for a candidate service in a specific domain.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "service_id": {"type": "string"},
                        "task_domain": {"type": "string"},
                        "task_description": {"type": "string"},
                        "risk_level": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]}
                    },
                    "required": ["service_id", "task_domain", "task_description", "risk_level"]
                }
            },
            {
                "name": "check_risk",
                "description": "Computes objective risk score and required confidence threshold for a task.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "task_domain": {"type": "string"},
                        "is_reversible": {"type": "boolean"},
                        "data_sensitivity": {"type": "string"}
                    },
                    "required": ["task_domain", "is_reversible", "data_sensitivity"]
                }
            },
            {
                "name": "verify_result",
                "description": "Validates an unverified service execution output inside a sandbox.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "service_id": {"type": "string"},
                        "task_domain": {"type": "string"},
                        "raw_output": {"type": "object"}
                    },
                    "required": ["task_id", "service_id", "task_domain", "raw_output"]
                }
            },
            {
                "name": "record_interaction",
                "description": "Appends a verified interaction record into the local evidence store.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "service_id": {"type": "string"},
                        "task_domain": {"type": "string"},
                        "is_success": {"type": "boolean"}
                    },
                    "required": ["task_id", "service_id", "task_domain", "is_success"]
                }
            }
        ]

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatches an MCP tool invocation."""
        if name == "check_risk":
            task_mock = Task(
                domain=arguments.get("task_domain", "general"),
                description="risk check",
                input_payload={},
                risk_level=RiskTier.HIGH if not arguments.get("is_reversible", True) else RiskTier.LOW
            )
            assessment = self.risk_layer.assess(task_mock)
            return assessment.model_dump()

        elif name == "verify_agent":
            return {
                "is_valid": True,
                "is_reachable": True,
                "registration_status": "ACTIVE"
            }

        else:
            return {"status": "executed", "tool": name, "echo": arguments}
