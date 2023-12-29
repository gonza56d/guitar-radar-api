from abc import ABC, abstractmethod
from uuid import UUID

from app.core.models.users import User


class UserRepository(ABC):

    @abstractmethod
    def get_user(self, user_id: UUID) -> User:
        """Contract to get user by id."""

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        """Contract to get user their by email."""
