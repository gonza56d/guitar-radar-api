from abc import ABC, abstractmethod


class Connector(ABC):

    @abstractmethod
    def get_status(self) -> bool | str:
        """Return if connection is ok and implementation."""
        pass
