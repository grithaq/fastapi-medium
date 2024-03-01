from .base import BaseModel


class SignUpSchema(BaseModel):
    id: str
    username: str
    email: str
    password: str