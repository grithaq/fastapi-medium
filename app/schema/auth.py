from .base import BaseModel


class SignUpSchema(BaseModel):
    username: str
    password: str