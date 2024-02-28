from pydantic import BaseModel
from typing import List, TypeVar

T = TypeVar('T')


class ResponseModel(BaseModel):
    message: str
    status: str
    data: List[T]


class PaginationResponseModel(BaseModel):
    current: int
    total: int