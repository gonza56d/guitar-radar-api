from uuid import UUID

from app.api.exceptions import AlreadyExistsAPIException
from tests.base import APITest


class TestBrands(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/brands'

    def test_create_brand(self):
        response = self.client.post(
            self.domain_prefix,
            json={
                'name': 'ibanez',
                'founded_in': 1957
            }
        )

        assert response.status_code == 201
        assert response.json()['name'] == 'ibanez'
        assert response.json()['founded_in'] == 1957
        created_id = response.json()['id']
        assert isinstance(UUID(created_id), UUID)

    def test_create_brand_already_exists_exception(self):
        self.client.post(self.domain_prefix, json={'name': 'schecter', 'founded_in': 1976})
        response = self.client.post(self.domain_prefix, json={'name': 'schecter'})
        assert response.status_code == 422
