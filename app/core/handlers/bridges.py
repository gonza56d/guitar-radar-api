from dataclasses import dataclass

from app.core.commands.bridges import CreateBridgeCommand
from app.core.models.guitars import Bridge
from app.core.repositories.bridges import BridgeRepository


@dataclass(kw_only=True)
class CreateBridgeHandler:

    bridge_repository: BridgeRepository

    def __call__(self, command: CreateBridgeCommand) -> Bridge:
        return self.bridge_repository.create_bridge(command)
