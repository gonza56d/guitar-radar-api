from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateBrandCommand:

    name: str
    founded_in: int | None = None


@dataclass
class GetBrandCommand:

    id: UUID
