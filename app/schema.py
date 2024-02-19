from pydantic import BaseModel, Field
from typing import List


class Product(BaseModel):
    id: int = Field(description="The ID of the product",)
    name: str = Field(description="The name of the product",)
    price: float = Field(description="The price of the product",)


class ListProduct(BaseModel):
    products: List[Product] = Field(description="The list of products")