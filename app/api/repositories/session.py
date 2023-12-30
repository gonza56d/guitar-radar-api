from typing import Any
from uuid import UUID

from app.api.repositories.base import RedisRepository
from app.core.repositories.session import SessionRepository


class SessionTokenRedisRepository(SessionRepository, RedisRepository):

    def set_user_session(self, key: str, user_id: UUID) -> None:
        self.set(key, str(user_id))

    def get_user_session(self, key: str) -> Any | None:
        return self.get(key)

    @property
    def namespace(self) -> str:
        return 'session_token'
