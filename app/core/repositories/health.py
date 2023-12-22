from abc import ABC, abstractmethod

from app.core.models.health import DependencyStatus


class HealthRepository(ABC):

    @abstractmethod
    def get_status(self) -> DependencyStatus:
        """Return if connection is ok and implementation."""
