from .base import BaseModel, ResponseModel
from .user import UserSchema


class CategorySchema(BaseModel):
    id: int
    name: str
    user: UserSchema


class ListCategoryResponse(ResponseModel):
    pass


class TodoCategorySchema(BaseModel):
    id: int
    name: str