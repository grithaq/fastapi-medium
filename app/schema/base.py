from typing import List, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel):
    message: str
    status: str
    data: List[T]


class PaginationResponseModel(BaseModel):
    current: int
    total: int
