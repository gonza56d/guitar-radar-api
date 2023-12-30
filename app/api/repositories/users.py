from uuid import UUID

from sqlalchemy import Table

from app.api.orm.mappings import users_table
from app.api.repositories.base import SQLRepository
from app.core.models.users import User
from app.core.repositories.users import UserRepository


class UserSQLRepository(UserRepository, SQLRepository):

    @property
    def table(self) -> Table | None:
        return users_table

    def get_user(self, user_id: UUID) -> User:
        raise NotImplemented()

    def get_user_by_email(self, email: str) -> User:
        return self._get_by_column(email, self.table.c.email, User)
