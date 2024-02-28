from .base import BaseModel, ResponseModel, PaginationResponseModel


class UserSchema(BaseModel):
    id: int
    name: str


class ListUserSchema(ResponseModel):
    pass


class ListUserResponse(ResponseModel):
    pagination: PaginationResponseModel