from .base import BaseModel
from typing import Union


class SignUpSchema(BaseModel):
    id: str
    username: str
    email: str
    password: str

class TokenData(BaseModel):
    username: Union[str, None] = None