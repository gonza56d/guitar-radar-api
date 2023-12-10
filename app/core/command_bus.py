from pymessagebus import CommandBus

from app.core.commands.bridges import CreateBridgeCommand
from app.core.handlers.bridges import CreateBridgeHandler

command_bus = CommandBus()
command_bus.add_handler(CreateBridgeCommand, CreateBridgeHandler)
