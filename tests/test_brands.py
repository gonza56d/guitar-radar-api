from uuid import UUID, uuid4

import pytest

from tests.base import APITest


class TestBrands(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/brands'

    def test_create_brand_ok(self):
        response = self.client.post(
            self.domain_prefix,
            **self.auth_headers,
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
        self.client.post(self.domain_prefix, **self.auth_headers, json={'name': 'schecter', 'founded_in': 1976})
        response = self.client.post(self.domain_prefix, **self.auth_headers, json={'name': 'schecter'})
        assert response.status_code == 422
        assert response.json() == {'message': 'Brand with name schecter already exists.'}

    @pytest.mark.parametrize('get_by', ['id', 'name'])
    def test_get_brand(self, get_by: str):
        created_response = self.client.post(
            self.domain_prefix,
            **self.auth_headers,
            json={'name': 'jackson', 'founded_in': 1980}
        )
        value_to_get_by = created_response.json().get(get_by)
        response = self.client.get(f'{self.domain_prefix}/{value_to_get_by}')
        assert response.json() == created_response.json()

    @pytest.mark.parametrize('get_by', ['id', 'name'])
    def test_get_brand_not_found(self, get_by: str):
        get_by_value = uuid4() if get_by == 'id' else 'fender'
        response = self.client.get(f'{self.domain_prefix}/{get_by_value}')
        assert response.status_code == 404
        assert response.json() == {
            'message': f'Brand by {get_by} {get_by_value} was not found.'
        }
