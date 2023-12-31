from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.api.serializers.auth import AuthRequest, AuthResponse
from app.containers import Container
from app.core.api_bus import APICommandBus
from app.core.models.auth import AuthToken

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('', status_code=201, response_model=AuthResponse)
@inject
async def authenticate(
        auth_request: AuthRequest,
        command_bus: APICommandBus = Depends(Provide[Container.command_bus])
):
    auth_token: AuthToken = command_bus.handle(auth_request.deserialize())
    return AuthResponse.serialize(auth_token)
