from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    password: str


class UserAllOptionalSchema(BaseModel):
    username: None | str
    password: None | str


@dataclass
class TokenData:
    sub: int
    exp: datetime | None = None


