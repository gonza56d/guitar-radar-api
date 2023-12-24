from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Any

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from sqlalchemy import (
    Engine,
    insert,
    literal_column,
    Table,
    text,
    UpdateBase,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.dml import ReturningInsert

from app.api.exceptions import AlreadyExistsAPIException


@dataclass
class SQLRepository(ABC):

    engine: Engine

    @property
    @abstractmethod
    def table(self) -> Table | None:
        """Override table used by implemented repository."""

    def _execute(
            self,
            stmt: UpdateBase | str,
            commit: bool,
            returning: type[object] | type[list] | type[None]
    ) -> dict[str, Any] | list[dict[str, Any]]:
        if isinstance(stmt, str):
            stmt = text(stmt)
        else:
            stmt.compile()
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if commit:
                conn.commit()
        columns = result.keys()
        if returning == list:
            return [dict(zip(columns, row)) for row in result.all()]
        if returning == object:
            return dict(zip(columns, result.first()))

    def _insert(
            self,
            instances: object | list[object],
            returning_class: Type | list[Type]
    ) -> Any | list[Any]:
        stmt = self.__build_insert_stmt(instances)
        try:
            cursor_result = self._execute(
                stmt,
                commit=True,
                returning=object if not isinstance(returning_class, list) else list
            )
        except IntegrityError as err:
            msg = err.args[0]
            key, value, _ = msg.split('Key ')[1].replace('(', '').replace('=', '').split(')')
            raise AlreadyExistsAPIException(returning_class.__name__, key, value)
        return (
            returning_class(**cursor_result)
            if not isinstance(returning_class, list) else
            [returning_class(**value) for value in cursor_result]
        )

    def __build_insert_stmt(self, instances: object | list[object]) -> ReturningInsert:
        values = (
            instances.__dict__
            if not isinstance(instances, list) else
            [instance.__dict__ for instance in instances]
        )
        stmt = insert(self.table).values(values).returning(literal_column('*'))
        return stmt


@dataclass
class MongoRepository(ABC):

    client: MongoClient
    database_name: str

    @property
    @abstractmethod
    def collection(self) -> Collection:
        """Get repository collection."""

    @property
    def database(self) -> Database:
        return self.client[self.database_name]
