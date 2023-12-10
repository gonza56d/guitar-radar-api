from dataclasses import dataclass
from uuid import UUID

from app.core.models.guitars import Bridge


@dataclass
class CreateBridgeCommand:

    brand_id: UUID
    name: str
    color_ids: list[UUID]
    year_of_introduction: int | None = None
