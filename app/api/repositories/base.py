from dataclasses import dataclass

from sqlalchemy import CursorResult, Engine, select, UpdateBase

from app.core.repositories.connectors import Connector


@dataclass(kw_only=True)
class SQLRepository(Connector):

    engine: Engine

    def _execute(
            self,
            stmt: UpdateBase | str,
            returning: list | None = None
    ) -> CursorResult:
        if not isinstance(stmt, str):
            stmt.compile()
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result

    def get_status(self) -> bool | str:
        """Get if connection is ok and implementation."""
        result = self._execute('SELECT 1')
