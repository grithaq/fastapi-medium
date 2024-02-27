from .base import BaseModel, ResponseModel
from .user import UserSchema


class CategorySchema(BaseModel):
    id: int
    name: str
    user: UserSchema


class CategoryRequestSchema(BaseModel):
    id: int
    name: str
    user_id: int


class ListCategoryResponse(ResponseModel):
    pass


class CreateCategoryResponse(ResponseModel):
    pass


class TodoCategorySchema(BaseModel):
    id: int
    name: str