from uuid import UUID

import bcrypt
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

    def is_password_valid(self, raw_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def _hash_password(self, raw_password: str) -> str:
        """Return hashed password given a raw password."""
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
