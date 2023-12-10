from abc import ABC, abstractmethod

from app.core.commands.bridges import CreateBridgeCommand
from app.core.models.guitars import Bridge


class BridgeRepository(ABC):

    @abstractmethod
    def create_bridge(self, bridge: CreateBridgeCommand) -> Bridge:
        pass
