from dataclasses import dataclass

from app.core.models.guitars import Bridge
from app.core.repositories.bridges import BridgeRepository


@dataclass(kw_only=True)
class CreateBridgeHandler:

    bridge_repository: BridgeRepository

    def __call__(self, bridge: Bridge) -> None:
        self.bridge_repository.create_bridge(bridge)
