from pydantic import BaseModel, Field
from typing import List, TypeVar

T = TypeVar('T')


class ResponseModel(BaseModel):
    message: str
    status: str
    data: List[T]


class Product(BaseModel):
    id: int = Field(description="The ID of the product",)
    name: str = Field(description="The name of the product",)
    price: float = Field(description="The price of the product",)


class ListProduct(ResponseModel):
    data: List[Product] = Field(description="The list of products")


class UserSchema(BaseModel):
    id: int
    name: str


class CategorySchema(BaseModel):
    id: int
    name: str
    user: UserSchema


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    categories: List[CategorySchema]
    user: UserSchema


class ListUserSchema(ResponseModel):
    pass


class ListCategoryResponse(ResponseModel):
    pass


class ListTodoResponse(ResponseModel):
    data: List[TodoSchema]