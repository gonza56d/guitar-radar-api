from datetime import datetime
from typing import Type

from pydantic import EmailStr

from app.api.serializers.base import RequestModel, ResponseModel
from app.core.commands.auth import AuthenticateCommand


class AuthRequest(RequestModel):

    email: EmailStr
    password: str

    @property
    def core_model(self) -> Type:
        return AuthenticateCommand


class AuthResponse(ResponseModel):

    access_token: str
    expiration: datetime
