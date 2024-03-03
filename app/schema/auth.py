from .base import BaseModel, ResponseModel
from typing import Union


class SignUpSchema(BaseModel):
    id: str
    username: str
    email: str
    password: str
    

class TokenData(BaseModel):
    username: Union[str, None] = None


class UserAuthSchema(BaseModel):
    id: str
    username: str
    email: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDb(UserAuthSchema):
    password: str


class MyProfileResponse(ResponseModel):
    data : UserAuthSchema