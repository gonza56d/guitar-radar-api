from pymongo.collection import Collection

from app.api.repositories.base import MongoRepository, SQLRepository
from app.api.env import Env
from app.core.repositories.health import HealthRepository
from app.core.models.health import DependencyStatus


class HealthSQLRepository(SQLRepository, HealthRepository):

    def get_status(self) -> DependencyStatus:
        """Get if connection is ok and implementation."""
        result = self._execute('SELECT 1', False, object)
        connected = result[0] == 1 if result else False
        return DependencyStatus(connected, Env.SQL_IMPL)


class HealthMongoRepository(MongoRepository, HealthRepository):

    @property
    def collection(self) -> Collection:
        return self.database['health']

    def get_status(self) -> DependencyStatus:
        """Get if connection is ok and implementation."""
        result = self.client.server_info()
        return DependencyStatus(result is not None, Env.DOCUMENT_IMPL)
