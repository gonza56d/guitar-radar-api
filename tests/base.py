from abc import ABC, abstractmethod

from fastapi.testclient import TestClient

from app.api.main import api


class APITest(ABC):

    @property
    def client(self) -> TestClient:
        return TestClient(api, base_url=f'http://localhost:8000{self.domain_prefix}')

    @property
    @abstractmethod
    def domain_prefix(self) -> str:
        """Prefix for the domain under test."""
