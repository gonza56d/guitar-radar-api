from abc import ABC, abstractmethod
from uuid import UUID

from app.core.models.auth import Auth


class AuthRepository(ABC):

    @abstractmethod
    def get_auth(self, user_id: UUID) -> Auth:
        """Get auth from given user id."""
