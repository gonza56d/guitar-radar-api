from abc import ABC, abstractmethod
from uuid import UUID

from app.core.commands.brands import CreateBrandCommand
from app.core.models.guitars import Brand


class BrandRepository(ABC):

    @abstractmethod
    def create_brand(self, brand: CreateBrandCommand) -> Brand:
        pass

    @abstractmethod
    def get_brand(self, id: UUID) -> Brand:
        pass
