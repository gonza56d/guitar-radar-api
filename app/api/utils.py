from typing import Annotated
from uuid import UUID

from fastapi import Header
import jwt
from jwt import DecodeError, InvalidSignatureError

from app.api.exceptions import UnauthorizedAPIException
from app.env import Env


async def request_session_token(authorization: Annotated[str, Header()]) -> UUID:
    try:
        decoded_jwt = jwt.decode(authorization, Env.CACHE_SESSION_SECRET_KEY, algorithms=['HS256'])
        user_id = UUID(decoded_jwt['user_id'])
    except DecodeError | InvalidSignatureError | KeyError | ValueError:
        raise UnauthorizedAPIException()
    return user_id
