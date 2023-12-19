from http import HTTPStatus

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.api.containers import Container
from app.core.api_bus import APICommandBus
from app.core.commands.health import GetHealthCommand


router = APIRouter(prefix='/health', tags=['health'])


@router.get('')
@inject
async def get_health(
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    health_status = await command_bus.handle(GetHealthCommand())
    return JSONResponse(
        content=health_status,
        status_code=(
            HTTPStatus.OK
            if health_status.overall_status.status == 'HEALTHY' else
            HTTPStatus.SERVICE_UNAVAILABLE
        )
    )
