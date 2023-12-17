from app.core.commands.health import GetHealthCommand
from app.core.models.health import HealthStatus, DependencyStatus
from app.core.repositories.connectors import Connector


class GetHealthHandler:

    sql_connection: Connector
    document_connection: Connector

    def __call__(self, command: GetHealthCommand) -> HealthStatus:
        sql_alive, sql_implementation = self.sql_connection.get_status()
        document_alive, document_implementation = self.document_connection.get_status()

        return HealthStatus(
            sql_db_status=DependencyStatus(sql_alive, document_implementation),
            document_db_status=DependencyStatus(document_alive, document_implementation)
        )
