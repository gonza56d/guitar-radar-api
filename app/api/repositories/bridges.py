from sqlalchemy import insert, select

from app.api.orm.guitars import bridge_table
from app.core.commands.bridges import CreateBridgeCommand
from app.core.models.guitars import Bridge
from app.core.repositories.bridges import BridgeRepository


class BridgeSQLRepository(BridgeRepository):

    table = bridge_table

    def create_bridge(self, bridge: CreateBridgeCommand) -> Bridge:
        insert_id = insert(self.table).values(**bridge.__dict__).returning(self.table.c.id)
        bridge_result = select(self.table).where(self.table.id == insert_id)
        # TODO: https://stackoverflow.com/questions/75107329/how-to-return-an-object-after-insert-with-sqlalchemy
