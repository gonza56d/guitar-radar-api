from dataclasses import dataclass
from uuid import UUID

from app.core.commands.base import CreateCommand


@dataclass
class CreateBridgeCommand(CreateCommand):

    brand_id: UUID
    name: str
    color_ids: list[UUID]
    year_of_introduction: int | None = None
