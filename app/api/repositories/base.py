from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Any
from uuid import UUID

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from redis import Redis
from sqlalchemy import (
    Column,
    Engine,
    insert,
    literal_column,
    select,
    Select,
    Table,
    text,
    UpdateBase,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.dml import ReturningInsert

from app.api.exceptions import AlreadyExistsAPIException, NotFoundAPIException


@dataclass
class SQLRepository(ABC):

    engine: Engine

    @property
    @abstractmethod
    def table(self) -> Table | None:
        """Override table used by implemented repository."""

    def _execute(
            self,
            stmt: Select | UpdateBase | str,
            commit: bool,
            returning: type[object] | type[list] | type[None]
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
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
            result = result.first()
            if not result:
                return None
            return dict(zip(columns, result))

    def _get(self, id: UUID, returning_class: Type) -> Any:
        stmt = select(self.table).where(self.table.c.id == id)
        return self.__execute_get(stmt, returning_class, 'id', id)

    def _get_by_name(self, name: str, returning_class: Type) -> Any:
        stmt = select(self.table).where(self.table.c.name == name)
        return self.__execute_get(stmt, returning_class, 'name', name)

    def _get_by_column(self, value: Any, column: Column, returning_class: Type) -> Any | None:
        stmt = select(self.table).where(column == value)
        return self.__execute_get(stmt, returning_class, column.name, value)

    def __execute_get(self, stmt, returning_class: Type, field: str, value: Any):
        cursor_result = self._execute(
            stmt,
            commit=False,
            returning=object
        )
        if cursor_result is None:
            raise NotFoundAPIException(returning_class.__name__, field, value)
        return returning_class(**cursor_result)

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


class RedisRepository(ABC):

    def __init__(self, client: Redis):
        self._client: Redis = client

    def get(self, key: str) -> str | dict:
        return self._client.get(self._get_key(key))

    def set(self, key: str, value: str | dict, expiration_minutes: int | None = None) -> None:
        if expiration_minutes is None:
            self._client.set(self._get_key(key), value)
        else:
            self._client.setex(self._get_key(key), expiration_minutes * 60, value)

    @property
    @abstractmethod
    def namespace(self) -> str:
        """Declare index name for repository implementation."""

    def _get_key(self, key: str) -> str:
        return f'{self.namespace}:{key}'
