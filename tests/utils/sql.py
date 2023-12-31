from dependency_injector.wiring import Provide, inject
from sqlalchemy import Engine, Table

from app.api.repositories.base import SQLRepository
from app.containers import Container


class SQLUtils(SQLRepository):

    @inject
    def __init__(self, table: Table, engine: Engine = Provide[Container.sql_engine]) -> None:
        self._table = table
        self.engine = engine

    @property
    def table(self) -> Table | None:
        return self._table

    @table.setter
    def table(self, value: str) -> None:
        self._table = value
