from .base import BaseModel, PaginationResponseModel, ResponseModel


class UserSchema(BaseModel):
    id: int
    username: str


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


class SignInResponse(BaseModel):
    access_token: str
    token_type: str
