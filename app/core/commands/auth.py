from dataclasses import dataclass


@dataclass
class AuthenticateCommand:

    email: str
    password: str
