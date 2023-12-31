from abc import ABC
from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateCommand(ABC):
    """Enforce tying the creation of a new object to a user."""

    user_id: UUID
