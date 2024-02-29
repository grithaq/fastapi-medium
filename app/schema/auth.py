from .base import BaseModel


class SignUpSchema(BaseModel):
    id: str = '1'
    username: str = "grithaq"
    email: str = 'grithaq@me.com'
    password: str = '123456'