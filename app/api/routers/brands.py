from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.api.serializers.brands import BrandResponse, CreateBrandRequest
from app.api.utils import request_session_token
from app.containers import Container
from app.core.api_bus import APICommandBus
from app.core.commands.brands import GetBrandCommand
from app.core.models.guitars import Brand

router = APIRouter(prefix='/brands', tags=['brands'])


@router.post('', status_code=201, response_model=BrandResponse)
@inject
async def create_brand(
        create_brand_request: CreateBrandRequest,
        user_id: Annotated[UUID, Depends(request_session_token)],
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    brand: Brand = command_bus.handle(create_brand_request.deserialize(user_id))
    return BrandResponse.serialize(brand)


@router.get('/{id_or_name}', status_code=200, response_model=BrandResponse)
@inject
async def get_brand(
        id_or_name: UUID | str,
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    try:
        command = GetBrandCommand(id=UUID(id_or_name))
    except ValueError:
        command = GetBrandCommand(name=id_or_name)

    brand: Brand = command_bus.handle(command)
    return BrandResponse.serialize(brand)
