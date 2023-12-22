from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from sqlalchemy import Engine, UpdateBase, Row, Sequence, text


@dataclass
class SQLRepository(ABC):

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
