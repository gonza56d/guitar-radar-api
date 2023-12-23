from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateBridgeCommand:

    brand_id: UUID
    name: str
    color_ids: list[UUID]
    year_of_introduction: int | None = None
