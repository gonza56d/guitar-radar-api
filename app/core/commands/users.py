from dataclasses import dataclass
from datetime import date


@dataclass
class CreateUserCommand:

    first_name: str
    last_name: str
    email: str
    password: str
    birth: date
