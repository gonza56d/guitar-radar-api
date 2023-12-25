from datetime import date
from typing import Type
from uuid import UUID

from pydantic import EmailStr

from app.api.serializers.base import ResponseModel, RequestModel
from app.core.commands.users import CreateUserCommand


class CreateUserRequest(RequestModel):

    first_name: str
    last_name: str
    email: EmailStr
    password: str
    birth: date

    @property
    def core_model(self) -> Type:
        return CreateUserCommand


class UserResponse(ResponseModel):

    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    birth: date
