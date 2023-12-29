from abc import ABC, abstractmethod

from app.core.commands.auth import AuthenticateCommand
from app.core.models.auth import AuthToken


class AuthRepository(ABC):

    @abstractmethod
    def authenticate(self, authentication: AuthenticateCommand) -> AuthToken:
        """User authentication contract."""
