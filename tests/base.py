from abc import ABC, abstractmethod
from datetime import date

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, Engine, text

from app.api.orm.mappings import auth_table, users_table
from app.core.commands.auth import CreateAuthCommand
from app.core.commands.users import CreateUserCommand
from app.core.models.auth import Auth
from app.core.models.users import User
from app.env import Env
from app.main import api
from tests.utils.auth import generate_auth_token, hash_password
from tests.utils.sql import SQLUtils


class APITest(ABC):

    def setup_method(self, test_method):
        """Cleanup database for the tests before executing."""
        with self.sql_engine.connect() as conn:
            with open('app/api/orm/sql_scripts/refresh_db.sql') as refresh_db_sql_script:
                query = text(refresh_db_sql_script.read())
                conn.execute(query)
                conn.commit()
        self.password = 'api_test_password'
        users_sql_utils = SQLUtils(users_table)
        auth_sql_utils = SQLUtils(auth_table)
        self.user: User = users_sql_utils._insert(
            CreateUserCommand(
                first_name='John',
                last_name='Rambo',
                email='johnrambo@apitest.com',
                birth=date(1996, 7, 1),
            ),
            User
        )
        auth_sql_utils._insert(
            CreateAuthCommand(
                user_id=self.user.id,
                password=hash_password(self.password)
            ),
            Auth
        )
        self.auth_token = generate_auth_token(self.user.id)
        self.auth_headers = {'headers': {'Authorization': self.auth_token}}

    @property
    def sql_engine(self) -> Engine:
        sql_db_url = f'{Env.SQL_IMPL}://{Env.SQL_USER}:{Env.SQL_PASSWORD}@{Env.SQL_SERVICE}/{Env.SQL_DB}'
        return create_engine(sql_db_url)

    @property
    def client(self) -> TestClient:
        return TestClient(api)

    @property
    @abstractmethod
    def domain_prefix(self) -> str:
        """Prefix for the domain under test."""
