from sqlalchemy import insert

from app.api.orm.guitars import bridge_table
from app.core.models.guitars import Bridge
from app.core.repositories.bridges import BridgeRepository


class BridgeSQLRepository(BridgeRepository):

    table = bridge_table

    def create_bridge(self, bridge: Bridge) -> None:
        insert(self.table).values(**bridge.__dict__)
