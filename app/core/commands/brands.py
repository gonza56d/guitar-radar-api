from dataclasses import dataclass


@dataclass
class CreateBrandCommand:

    name: str
    founded_in: int | None = None
