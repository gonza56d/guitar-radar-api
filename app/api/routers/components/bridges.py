from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pymessagebus import CommandBus

from app.api.serializers.bridges import CreateBridgeRequest
from app.api.utils import request_session_token
from app.containers import Container

router = APIRouter(prefix='/bridges', tags=['bridges'])


@inject
@router.post('')
async def create_bridge(
        create_bridge_request: CreateBridgeRequest,
        user_id: Annotated[UUID, Depends(request_session_token)],
        command_bus: CommandBus = Depends(Provide[Container.command_bus])
):
    command_bus.handle(create_bridge_request.deserialize(user_id))
    return JSONResponse(content={}, status_code=201)
