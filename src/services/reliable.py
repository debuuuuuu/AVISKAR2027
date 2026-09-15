import random
import time
from src.services.base import BaseServiceAgent
from src.data_models import Task, Interaction, BehaviorClass, Service


class ReliableServiceAgent(BaseServiceAgent):
    """
    Simulated reliable service provider.
    Exhibits consistent schema compliance, high availability (98%),
    and low execution latency (~120ms).
    """

    def __init__(self, service_metadata: Service, seed: int = 42):
        super().__init__(service_metadata)
        self.rng = random.Random(seed)

    def execute(self, task: Task) -> Interaction:
        # Latency model: Normal(120ms, 15ms)
        latency = max(20.0, self.rng.gauss(120.0, 15.0))
        
        # 98% availability
        if self.rng.random() > 0.98:
            return Interaction(
                task_id=task.task_id,
                service_id=self.service_id,
                client_id="orchestrator",
                dispatched_payload=task.input_payload,
                returned_payload=None,
                latency_ms=latency,
                status_code=503,
                timeout_occurred=True
            )

        # 96% accuracy
        is_accurate = self.rng.random() <= 0.96
        
        if task.domain == "math_computation":
            result_val = task.input_payload.get("expression_result", 42.0)
            if not is_accurate:
                result_val += 1.0  # Slight rounding or calculation error
            payload = {"status": "success", "result": result_val}
            
        elif task.domain == "code_execution":
            code_func = task.input_payload.get("expected_code", "def solution(): return True")
            if not is_accurate:
                code_func = "def solution(): return False"
            payload = {"status": "success", "code": code_func}
            
        elif task.domain == "schema_transformation":
            payload = {
                "status": "success",
                "transformed_data": task.input_payload.get("raw_data", {}),
                "is_valid_schema": is_accurate
            }
        else:
            payload = {"status": "success", "output": "valid_output" if is_accurate else "imprecise_output"}

        return Interaction(
            task_id=task.task_id,
            service_id=self.service_id,
            client_id="orchestrator",
            dispatched_payload=task.input_payload,
            returned_payload=payload,
            latency_ms=latency,
            status_code=200,
            timeout_occurred=False
        )
