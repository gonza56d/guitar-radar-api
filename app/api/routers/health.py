from http import HTTPStatus

from app.core.commands.health import GetHealthCommand
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pymessagebus import CommandBus

from app.api.container import Container


router = APIRouter(prefix='/health', tags=['health'])


@inject
@router.get('')
async def get_health(command_bus: CommandBus = Depends(Provide[Container])):
    health_status = command_bus.handle(GetHealthCommand())
    return JSONResponse(
        content=health_status,
        status_code=(
            HTTPStatus.OK
            if health_status.overall_status.status == 'HEALTHY' else
            HTTPStatus.SERVICE_UNAVAILABLE
        )
    )
