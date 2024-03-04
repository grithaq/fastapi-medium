from .base import BaseModel, PaginationResponseModel, ResponseModel


class CategorySchema(BaseModel):
    id: int
    name: str


class CategoryRequestSchema(BaseModel):
    id: int
    name: str


class ListCategoryResponse(ResponseModel):
    user_id: int


class CreateCategoryResponse(ResponseModel):
    pass


class TodoCategorySchema(BaseModel):
    id: int
    name: str


class CategoriesResponse(ListCategoryResponse):
    pagination: PaginationResponseModel
