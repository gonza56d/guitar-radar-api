from dataclasses import dataclass

from sqlalchemy import CursorResult, Engine


@dataclass(kw_only=True)
class SQLRepository:

    engine: Engine

    def _execute(self, stmt, returning: list | None = None) -> CursorResult:
        stmt.compile()
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result
