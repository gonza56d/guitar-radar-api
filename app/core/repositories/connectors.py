from abc import ABC, abstractmethod
from typing import Any


class Connector(ABC):

    @abstractmethod
    def get_status(self) -> Any:
        """Return if connection is ok and implementation."""
        pass
