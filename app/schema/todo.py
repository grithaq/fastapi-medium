from .base import BaseModel, ResponseModel, List, T
from .category import TodoCategorySchema
from .user import UserSchema


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    categories: List[TodoCategorySchema]
    user: UserSchema


class ListTodoResponse(ResponseModel):
    data: List[TodoSchema]