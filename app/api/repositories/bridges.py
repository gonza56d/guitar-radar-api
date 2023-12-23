from dataclasses import dataclass

from sqlalchemy import insert, Table

from app.api.orm.guitars import bridge_table
from app.api.repositories.base import SQLRepository
from app.core.commands.bridges import CreateBridgeCommand
from app.core.models.guitars import Bridge
from app.core.repositories.bridges import BridgeRepository


@dataclass
class BridgeSQLRepository(BridgeRepository, SQLRepository):

    @property
    def table(self) -> Table:
        return bridge_table

    def create_bridge(self, bridge: CreateBridgeCommand) -> Bridge:
        stmt = insert(self.table).values(**bridge.__dict__).returning()
        cursor_result = self._execute(stmt, commit=True, returning=object)
        return Bridge(*cursor_result)
