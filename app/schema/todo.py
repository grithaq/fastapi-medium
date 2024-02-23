from .base import BaseModel, ResponseModel, List
from .category import CategorySchema
from .user import UserSchema


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    categories: List[CategorySchema]
    user: UserSchema


class ListTodoResponse(ResponseModel):
    pass