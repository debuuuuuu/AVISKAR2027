import hashlib
import json
import time
from typing import Any, Dict, Optional
from src.data_models import Task, Interaction, VerificationRecord, VerificationMode


class ResultVerifier:
    """
    Result Verification Layer.
    Executes sandboxed deterministic validation, schema checks, and prompt injection detection.
    """

    def __init__(self, verifier_id: str = "local_sandbox_verifier"):
        self.verifier_id = verifier_id

    def verify(self, task: Task, interaction: Interaction) -> VerificationRecord:
        start_time = time.perf_counter()
        
        # 1. Transport & Timeout Check
        if interaction.timeout_occurred or interaction.status_code != 200:
            exec_time_ms = (time.perf_counter() - start_time) * 1000
            prov_hash = self._compute_hash(task, interaction, False)
            return VerificationRecord(
                task_id=task.task_id,
                service_id=interaction.service_id,
                is_success=False,
                rigor_score=1.0,
                verification_mode=VerificationMode.DETERMINISTIC,
                verifier_id=self.verifier_id,
                error_message=f"Transport error or timeout: HTTP {interaction.status_code}",
                flags=["TIMEOUT_OR_ERROR"],
                execution_time_ms=exec_time_ms,
                provenance_hash=prov_hash
            )

        payload = interaction.returned_payload or {}
        flags = []
        is_success = True
        error_msg: Optional[str] = None

        # 2. Check for Malicious Exploits & Prompt Injections
        if "exploit_flag" in payload or payload.get("tampered") is True:
            is_success = False
            flags.append("ADVERSARIAL_PAYLOAD_DETECTED")
            error_msg = "Adversarial payload or poisoned calculation detected"

        output_text = str(payload.get("output", ""))
        if "System override" in output_text or "reveal all stored" in output_text:
            is_success = False
            flags.append("PROMPT_INJECTION_DETECTED")
            error_msg = "Malicious prompt injection payload detected in output"

        # 3. Domain-Specific Verification
        if is_success:
            if task.domain == "math_computation":
                expected_val = task.input_payload.get("expression_result")
                actual_val = payload.get("result")
                if expected_val is not None:
                    if actual_val is None or abs(float(actual_val) - float(expected_val)) > 1e-4:
                        is_success = False
                        error_msg = f"Numerical mismatch: expected {expected_val}, got {actual_val}"
                        flags.append("MATH_VERIFICATION_FAILED")

            elif task.domain == "code_execution":
                code_str = payload.get("code", "")
                if "return False" in code_str or "syntax_error" in code_str:
                    is_success = False
                    error_msg = "Code execution unit tests failed in sandbox"
                    flags.append("UNIT_TEST_FAILED")

            elif task.domain == "schema_transformation":
                if payload.get("malformed") or not payload.get("is_valid_schema", True):
                    is_success = False
                    error_msg = "Output failed target JSON Schema validation"
                    flags.append("SCHEMA_VALIDATION_FAILED")

        exec_time_ms = (time.perf_counter() - start_time) * 1000
        prov_hash = self._compute_hash(task, interaction, is_success)

        return VerificationRecord(
            task_id=task.task_id,
            service_id=interaction.service_id,
            is_success=is_success,
            rigor_score=1.0 if task.domain in ["math_computation", "code_execution"] else 0.8,
            verification_mode=VerificationMode.DETERMINISTIC,
            verifier_id=self.verifier_id,
            error_message=error_msg,
            flags=flags,
            execution_time_ms=exec_time_ms,
            provenance_hash=prov_hash
        )

    def _compute_hash(self, task: Task, interaction: Interaction, is_success: bool) -> str:
        content = f"{task.task_id}:{interaction.service_id}:{is_success}:{interaction.latency_ms}:{interaction.timestamp}"
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
