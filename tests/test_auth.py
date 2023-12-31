from datetime import date
from uuid import UUID

import jwt
import pytest

from app.api.orm.mappings import auth_table, users_table
from app.core.commands.auth import CreateAuthCommand
from app.core.commands.users import CreateUserCommand
from app.core.models.auth import Auth
from app.core.models.users import User
from app.env import Env
from tests.base import APITest
from tests.utils.hashing import hash_password
from tests.utils.sql import SQLUtils


class TestAuth(APITest):

    def setup_method(self, test_method):
        super().setup_method(test_method)
        self.password = 'api_test_password'
        self.users_sql_utils = SQLUtils(users_table)
        self.auth_sql_utils = SQLUtils(auth_table)
        self.user: User = self.users_sql_utils._insert(
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
                user_id=self.user.id,
                password=hash_password(self.password)
            ),
            Auth
        )

    @property
    def domain_prefix(self) -> str:
        return '/auth'

    def test_authenticate(self):
        response = self.client.post(
            self.domain_prefix,
            json={
                'email': self.user.email,
                'password': self.password
            }
        )

        assert response.status_code == 201
        jwt_token = response.json()['access_token']
        decoded_token = jwt.decode(jwt_token, Env.CACHE_SESSION_SECRET_KEY, algorithms=['HS256'])
        assert UUID(decoded_token['user_id']) == self.user.id

    @pytest.mark.parametrize(
        'correct_email, correct_password',
        [(True, False), (False, True), (False, False)]
    )
    def test_authenticate_wrong_credentials(self, correct_email: bool, correct_password: bool):
        response = self.client.post(
            self.domain_prefix,
            json={
                'email': self.user.email if correct_email else 'wrong@email.com',
                'password': self.password if correct_password else 'wrong_password'
            }
        )

        assert response.status_code == 401
        assert response.json() == {'message': 'Invalid email or password.'}
