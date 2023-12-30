from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class SessionRepository(ABC):

    secret_key: str

    @abstractmethod
    def set_user_session(self, user_id: UUID) -> Any:
        """Contract for setting new session for given user."""

    @abstractmethod
    def get_user_session(self, key: str) -> Any | None:
        """Contract for getting current user session"""
