from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.api.serializers.brands import BrandResponse, CreateBrandRequest
from app.containers import Container
from app.core.api_bus import APICommandBus
from app.core.commands.brands import GetBrandCommand
from app.core.models.guitars import Brand

router = APIRouter(prefix='/brands', tags=['brands'])


@router.post('', status_code=201, response_model=BrandResponse)
@inject
async def create_brand(
        create_brand_request: CreateBrandRequest,
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    brand: Brand = command_bus.handle(create_brand_request.deserialize())
    return BrandResponse.serialize(brand)


@router.get('/{id}', status_code=200, response_model=BrandResponse)
@inject
async def get_brand(
        id: UUID,
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    brand: Brand = command_bus.handle(GetBrandCommand(id=id))
    return BrandResponse.serialize(brand)
