from abc import ABC, abstractmethod
from typing import Any, Dict
from src.data_models import Service, Task, Interaction, BehaviorClass


class BaseServiceAgent(ABC):
    """Abstract base class for simulated service providers."""

    def __init__(self, service_metadata: Service):
        self.metadata = service_metadata

    @property
    def service_id(self) -> str:
        return self.metadata.agent_id

    @property
    def behavior_class(self) -> BehaviorClass:
        return self.metadata.behavior_class

    @abstractmethod
    def execute(self, task: Task) -> Interaction:
        """Execute the delegated task and return an Interaction record."""
        pass
