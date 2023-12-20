from dataclasses import dataclass

from app.core.commands import GetHealthCommand
from app.core.models.health import DependencyStatus, HealthStatus
from app.core.repositories.connectors import Connector


@dataclass
class GetHealthHandler:

    sql_connection: Connector

    async def __call__(self, command: GetHealthCommand) -> HealthStatus:
        sql_db_status = self.sql_connection.get_status()

        return HealthStatus(
            sql_db_status=sql_db_status,
            document_db_status=DependencyStatus(True, 'Mock')
        )
