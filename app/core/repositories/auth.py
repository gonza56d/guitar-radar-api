from abc import ABC, abstractmethod
from uuid import UUID

from app.core.models.auth import Auth


class AuthRepository(ABC):

    @abstractmethod
    def get_auth(self, user_id: UUID) -> Auth:
        """Get auth from given user id."""

    @abstractmethod
    def is_password_valid(self, raw_password: str, hashed_password: str) -> bool:
        """Implement password validation."""

    @abstractmethod
    def _hash_password(self, raw_password: str) -> str:
        """Implement password hashing."""
