from http import HTTPStatus

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response

from app.api.containers import Container
from app.api.serializers.health import HealthStatusResponse
from app.core.api_bus import APICommandBus
from app.core.commands.health import GetHealthCommand
from app.core.models.health import HealthStatus

router = APIRouter(prefix='/health', tags=['health'])


@router.get('', response_model=HealthStatusResponse)
@inject
async def get_health(
        response: Response,
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    health_status: HealthStatus = await command_bus.handle(GetHealthCommand())
    response.status_code = (
        HTTPStatus.OK
        if health_status.overall_status.status == 'HEALTHY' else
        HTTPStatus.SERVICE_UNAVAILABLE
    )
    return HealthStatusResponse.serialize(health_status)
