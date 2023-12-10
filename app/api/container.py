from dependency_injector import containers, providers

from app.api.repositories.bridges import BridgeSQLRepository
from app.core.repositories.bridges import BridgeRepository
from app.core.command_bus import command_bus


class Container(containers.DeclarativeContainer):

    bridge_repository: BridgeRepository = providers.Singleton(BridgeSQLRepository)
    command_bus = command_bus
