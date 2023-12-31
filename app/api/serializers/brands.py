from typing import Type
from uuid import UUID

from app.api.serializers.base import ResponseModel, RequestModel
from app.core.commands import CreateBrandCommand


class BrandResponse(ResponseModel):

    id: UUID
    name: str
    founded_in: int | None = None
    user_id: UUID


class CreateBrandRequest(RequestModel):

    name: str
    founded_in: int | None = None

    @property
    def core_model(self) -> Type:
        return CreateBrandCommand
