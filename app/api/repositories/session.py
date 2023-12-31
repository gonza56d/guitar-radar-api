from dataclasses import dataclass
from datetime import datetime, timedelta
from time import time
from typing import Any
from uuid import UUID

import jwt

from app.api.repositories.base import RedisRepository
from app.core.repositories.session import SessionRepository


@dataclass
class SessionTokenRedisRepository(SessionRepository, RedisRepository):

    secret_key: str
    token_expiration_minutes: int

    def set_user_session(self, user_id: UUID) -> str:
        jwt_token = self._build_jwt_token(user_id)
        self.set(
            key=jwt_token,
            value=str(user_id),
            expiration_minutes=self.token_expiration_minutes
        )
        return jwt_token

    def get_user_session(self, key: str) -> Any | None:
        return self.get(key)

    @property
    def namespace(self) -> str:
        return 'session_token'

    def _build_jwt_token(self, user_id: UUID) -> str:
        jwt_token_payload = {
            'user_id': str(user_id),
            'exp': int(time()) + self.token_expiration_minutes * 60,
            'exp_datetime_utc': (datetime.utcnow() + timedelta(minutes=self.token_expiration_minutes)).isoformat()
        }
        return jwt.encode(jwt_token_payload, self.secret_key, algorithm='HS256')
