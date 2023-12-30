from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class SessionRepository(ABC):

    @abstractmethod
    def set_user_session(self, key: str, user_id: UUID) -> None:
        """Contract for setting new session for given user."""

    @abstractmethod
    def get_user_session(self, key: str) -> Any | None:
        """Contract for getting current user session"""
