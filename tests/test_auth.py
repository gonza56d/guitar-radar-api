from datetime import date
from uuid import uuid4

from app.api.orm.mappings import auth_table, users_table
from app.core.commands.auth import CreateAuthCommand
from app.core.commands.users import CreateUserCommand
from app.core.models.auth import Auth
from app.core.models.users import User
from tests.base import APITest
from tests.utils.hashing import hash_password
from tests.utils.sql import SQLUtils


class TestAuth(APITest):

    def setup_method(self, test_method):
        super().setup_method(test_method)
        self.password = 'api_test_password'
        self.users_sql_utils = SQLUtils(users_table)
        self.auth_sql_utils = SQLUtils(auth_table)

    @property
    def domain_prefix(self) -> str:
        return '/auth'

    def test_authenticate(self):
        user = self.users_sql_utils._insert(
            CreateUserCommand(
                first_name='John',
                last_name='Rambo',
                email='johnrambo@apitest.com',
                birth=date(1996, 7, 1),
            ),
            User
        )
        self.auth_sql_utils._insert(
            CreateAuthCommand(
                user_id=user.id,
                password=hash_password(self.password)
            ),
            Auth
        )

        response = self.client.post(
            self.domain_prefix,
            json={
                'email': user.email,
                'password': self.password
            }
        )

        assert response.status_code == 201
