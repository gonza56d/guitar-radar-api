from uuid import UUID

from tests.base import APITest


class TestBrands(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/brands'

    def test_create_brand(self):
        response = self.client.post(
            '',
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
