from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Auth:

    id: UUID
    user_id: UUID
    password: str


@dataclass
class AuthToken:

    access_token: str
