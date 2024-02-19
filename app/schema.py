from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    price: float


class ListProduct(BaseModel):
    products: List[Product]