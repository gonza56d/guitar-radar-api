from uuid import UUID

from sqlalchemy import Table

from app.api.orm.mappings import auth_table
from app.api.repositories.base import SQLRepository
from app.core.models.auth import Auth
from app.core.repositories.auth import AuthRepository


class AuthSQLRepository(AuthRepository, SQLRepository):

    @property
    def table(self) -> Table | None:
        return auth_table

    def get_auth(self, user_id: UUID) -> Auth:
        return self._get_by_column(user_id, self.table.c.user_id, Auth)
