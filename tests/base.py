from abc import ABC, abstractmethod

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, Engine, text

from app.env import Env
from app.main import api


class APITest(ABC):

    def setup_method(self, test_method):
        """Cleanup database for the tests before executing."""
        with self.sql_engine.connect() as conn:
            with open('app/api/orm/sql_scripts/refresh_db.sql') as refresh_db_sql_script:
                query = text(refresh_db_sql_script.read())
                conn.execute(query)
                conn.commit()

    @property
    def sql_engine(self) -> Engine:
        sql_db_url = f'{Env.SQL_IMPL}://{Env.SQL_USER}:{Env.SQL_PASSWORD}@{Env.SQL_SERVICE}/{Env.SQL_DB}'
        return create_engine(sql_db_url)

    @property
    def client(self) -> TestClient:
        return TestClient(api, base_url=f'http://localhost:8000{self.domain_prefix}')

    @property
    @abstractmethod
    def domain_prefix(self) -> str:
        """Prefix for the domain under test."""
