from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pymessagebus import CommandBus

from app.api.containers import Container
from app.core.commands.bridges import CreateBridgeCommand
from app.core.models.guitars import Bridge

router = APIRouter(prefix='/bridges', tags=['bridges'])


@inject
@router.post('')
async def post_bridge(
        bridge: CreateBridgeCommand,
        command_bus: CommandBus = Depends(Provide[Container.command_bus])
):
    command_bus.handle(bridge)
    return JSONResponse(content={}, status_code=201)
