from abc import ABC, abstractmethod

from app.core.models.guitars import Bridge


class BridgeRepository(ABC):

    @abstractmethod
    def create_bridge(self, bridge: Bridge) -> None:
        pass
