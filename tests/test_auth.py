from uuid import UUID

import jwt
import pytest

from app.env import Env
from tests.base import APITest


class TestAuth(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/auth'

    def test_authenticate_ok(self):
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
