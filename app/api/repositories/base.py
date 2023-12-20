from dataclasses import dataclass

from sqlalchemy import Engine, UpdateBase, Row, Sequence, text

from app.api.env import Env
from app.core.models.health import DependencyStatus
from app.core.repositories.connectors import Connector


@dataclass
class SQLRepository(Connector):

    engine: Engine

    def _execute(
            self,
            stmt: UpdateBase | str,
            commit: bool,
            returning: type[object] | type[list] | type[None]
    ) -> Row | Sequence[Row] | None:
        if isinstance(stmt, str):
            stmt = text(stmt)
        else:
            stmt.compile()
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if commit:
                conn.commit()
        if returning == list:
            return result.all()
        if returning == object:
            return result.first()

    def get_status(self) -> DependencyStatus:
        """Get if connection is ok and implementation."""
        result = self._execute('SELECT 1', False, object)
        connected = result[0] == 1 if result else False
        return DependencyStatus(connected, Env.SQL_IMPL)
