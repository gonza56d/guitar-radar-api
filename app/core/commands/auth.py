from dataclasses import dataclass
from uuid import UUID


@dataclass
class AuthenticateCommand:

    email: str
    password: str


@dataclass
class CreateAuthCommand:

    user_id: UUID
    password: str
