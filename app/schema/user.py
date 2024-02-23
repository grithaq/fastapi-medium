from .base import BaseModel, ResponseModel


class UserSchema(BaseModel):
    id: int
    name: str


class ListUserSchema(ResponseModel):
    pass
