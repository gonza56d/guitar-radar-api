from dataclasses import dataclass
import bcrypt

from app.api.exceptions import NotFoundAPIException, UnauthorizedAPIException
from app.core.commands.auth import AuthenticateCommand
from app.core.models.auth import AuthToken
from app.core.repositories.auth import AuthRepository
from app.core.repositories.users import UserRepository


@dataclass(kw_only=True)
class AuthenticateHandler:

    auth_repository: AuthRepository
    user_repository: UserRepository

    def __call__(self, command: AuthenticateCommand) -> AuthToken:
        try:
            user = self.user_repository.get_user_by_email(command.email)
            auth = self.auth_repository.get_auth(user.id)
        except NotFoundAPIException:
            raise UnauthorizedAPIException()
        if not self.__is_password_valid(command.password, auth.password):
            raise UnauthorizedAPIException()
        # TODO: generate auth token

    def __hash_password(self, raw_password: str) -> str:
        """Return hashed password given a raw password."""
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def __is_password_valid(self, raw_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))
