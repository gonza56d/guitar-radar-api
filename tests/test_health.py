from http import HTTPStatus

from tests.base import APITest


class TestHealth(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/health'

    def test_health(self):
        response = self.client.get('')
        assert response.status_code == HTTPStatus.OK
