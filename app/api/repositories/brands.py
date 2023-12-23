from dataclasses import dataclass

from sqlalchemy import insert, Table

from app.api.orm.guitars import brand_table
from app.api.repositories.base import SQLRepository
from app.core.commands.brands import CreateBrandCommand
from app.core.models.guitars import Brand
from app.core.repositories.brands import BrandRepository


@dataclass
class BrandSQLRepository(BrandRepository, SQLRepository):

    @property
    def table(self) -> Table:
        return brand_table

    def create_brand(self, brand: CreateBrandCommand) -> Brand:
        stmt = insert(self.table).values(**brand.__dict__).returning()
        cursor_result = self._execute(stmt, commit=True, returning=object)
        return Brand(*cursor_result)
