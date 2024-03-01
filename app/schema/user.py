from .base import BaseModel, ResponseModel, PaginationResponseModel


class UserSchema(BaseModel):
    id: int
    name: str


class ListUserSchema(ResponseModel):
    pass


class ListUserResponse(ResponseModel):
    pagination: PaginationResponseModel


class AccountSchema(BaseModel):
    id: str
    username: str
    email: str


class SignUpResponse(BaseModel):
    message: str
    status: str
    account: AccountSchema
    
