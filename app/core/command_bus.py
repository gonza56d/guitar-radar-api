from pymessagebus import CommandBus

from app.core.commands.health import GetHealthCommand
from app.core.commands.bridges import CreateBridgeCommand
from app.core.handlers.bridges import CreateBridgeHandler
from app.core.handlers.health import GetHealthHandler


command_bus = CommandBus()
command_bus.add_handler(CreateBridgeCommand, CreateBridgeHandler)
command_bus.add_handler(GetHealthCommand, GetHealthHandler)
