from dataclasses import dataclass

from app.core.commands.brands import CreateBrandCommand, GetBrandCommand
from app.core.models.guitars import Brand
from app.core.repositories.brands import BrandRepository


@dataclass(kw_only=True)
class CreateBrandHandler:

    brand_repository: BrandRepository

    def __call__(self, command: CreateBrandCommand) -> Brand:
        return self.brand_repository.create_brand(command)


@dataclass(kw_only=True)
class GetBrandHandler:

    brand_repository: BrandRepository

    def __call__(self, command: GetBrandCommand) -> Brand:
        return self.brand_repository.get_brand(
            command.id
        )
