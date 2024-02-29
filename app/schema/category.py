from .base import BaseModel, ResponseModel, PaginationResponseModel
from .user import UserSchema


class CategorySchema(BaseModel):
    id: int
    name: str


class CategoryRequestSchema(BaseModel):
    id: int
    name: str


class ListCategoryResponse(ResponseModel):
    pass


class CreateCategoryResponse(ResponseModel):
    pass


class TodoCategorySchema(BaseModel):
    id: int
    name: str


class CategoriesResponse(ListCategoryResponse):
    pagination: PaginationResponseModel