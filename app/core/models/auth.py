from dataclasses import dataclass
from uuid import UUID


@dataclass
class Auth:

    id: UUID
    user_id: UUID
    password: str
