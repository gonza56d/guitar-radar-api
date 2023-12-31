from dataclasses import dataclass

from app.core.commands.auth import AuthenticateCommand
from app.core.exceptions import UnauthorizedException, NotFoundException
from app.core.models.auth import AuthToken
from app.core.repositories.auth import AuthRepository
from app.core.repositories.session import SessionRepository
from app.core.repositories.users import UserRepository


@dataclass(kw_only=True)
class AuthenticateHandler:

    auth_repository: AuthRepository
    user_repository: UserRepository
    session_repository: SessionRepository

    def __call__(self, command: AuthenticateCommand) -> AuthToken:
        try:
            user = self.user_repository.get_user_by_email(command.email)
            auth = self.auth_repository.get_auth(user.id)
        except NotFoundException:
            raise UnauthorizedException()
        if not self.auth_repository.is_password_valid(command.password, auth.password):
            raise UnauthorizedException()

        session_token = self.session_repository.set_user_session(user.id)
        return AuthToken(access_token=session_token)
