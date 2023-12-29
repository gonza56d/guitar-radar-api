from dataclasses import dataclass

from app.core.commands.auth import AuthenticateCommand
from app.core.models.auth import AuthToken
from app.core.repositories.auth import AuthRepository


@dataclass(kw_only=True)
class AuthenticateHandler:

    auth_repository: AuthRepository

    def __call__(self, command: AuthenticateCommand) -> AuthToken:
        return self.auth_repository.authenticate(command)
