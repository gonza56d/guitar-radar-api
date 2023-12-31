from typing import Type
from uuid import UUID

from app.api.serializers.base import RequestModel
from app.core.commands import CreateBridgeCommand


class CreateBridgeRequest(RequestModel):

    brand_id: UUID
    name: str
    color_ids: list[UUID]
    year_of_introduction: int | None = None

    @property
    def core_model(self) -> Type:
        return CreateBridgeCommand
