from pydantic import BaseModel, Field
from typing import List


class ResponseModel(BaseModel):
    message: str
    status: str


class Product(BaseModel):
    id: int = Field(description="The ID of the product",)
    name: str = Field(description="The name of the product",)
    price: float = Field(description="The price of the product",)


class ListProduct(BaseModel):
    products: List[Product] = Field(description="The list of products")


class UserSchema(BaseModel):
    id: int
    name: str
    email: str


class ListUserSchema(BaseModel):
    users: List[UserSchema]


class CategorySchema(BaseModel):
    id: int
    name: str


class ListCategoryResponse(ResponseModel):
    categories: List[CategorySchema]