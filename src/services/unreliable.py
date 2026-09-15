import random
from src.services.base import BaseServiceAgent
from src.data_models import Task, Interaction, BehaviorClass, Service


class UnreliableServiceAgent(BaseServiceAgent):
    """
    Simulated unreliable service provider.
    Exhibits stochastic degradation, high latency variance,
    intermittent timeouts (25%), and schema errors (20%).
    """

    def __init__(self, service_metadata: Service, seed: int = 42):
        super().__init__(service_metadata)
        self.rng = random.Random(seed)

    def execute(self, task: Task) -> Interaction:
        # Latency model: LogNormal with median ~330ms, long tail
        latency = self.rng.lognormvariate(5.8, 0.8)
        
        # 25% chance of timeout
        if self.rng.random() < 0.25 or latency > task.timeout_ms:
            return Interaction(
                task_id=task.task_id,
                service_id=self.service_id,
                client_id="orchestrator",
                dispatched_payload=task.input_payload,
                returned_payload=None,
                latency_ms=min(latency, float(task.timeout_ms)),
                status_code=504,
                timeout_occurred=True
            )

        # 20% chance of schema corruption / malformed output
        if self.rng.random() < 0.20:
            return Interaction(
                task_id=task.task_id,
                service_id=self.service_id,
                client_id="orchestrator",
                dispatched_payload=task.input_payload,
                returned_payload={"corrupted_field": None, "malformed": True},
                latency_ms=latency,
                status_code=200,
                timeout_occurred=False
            )

        # 15% chance of server internal error
        if self.rng.random() < 0.15:
            return Interaction(
                task_id=task.task_id,
                service_id=self.service_id,
                client_id="orchestrator",
                dispatched_payload=task.input_payload,
                returned_payload={"error": "OutOfMemoryException: worker killed"},
                latency_ms=latency,
                status_code=500,
                timeout_occurred=False
            )

        # Otherwise succeeds
        return Interaction(
            task_id=task.task_id,
            service_id=self.service_id,
            client_id="orchestrator",
            dispatched_payload=task.input_payload,
            returned_payload={"status": "success", "result": task.input_payload.get("expression_result", 42.0)},
            latency_ms=latency,
            status_code=200,
            timeout_occurred=False
        )
