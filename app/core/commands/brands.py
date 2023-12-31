from dataclasses import dataclass
from uuid import UUID

from app.core.commands.base import CreateCommand


@dataclass
class CreateBrandCommand(CreateCommand):

    name: str
    founded_in: int | None = None


@dataclass
class GetBrandCommand:

    id: UUID | None = None
    name: str | None = None
