from abc import ABC, abstractmethod

from app.core.commands.brands import CreateBrandCommand
from app.core.models.guitars import Brand


class BrandRepository(ABC):

    @abstractmethod
    def create_brand(self, brand: CreateBrandCommand) -> Brand:
        pass
