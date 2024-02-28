from .base import BaseModel, List, T
from .category import TodoCategorySchema
from .user import UserSchema


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    categories: List[TodoCategorySchema]
    user: UserSchema


class TodoRequestSchema(BaseModel):
    id: int
    title: str
    description: str
    categories: List[T]
    user_id: int


class ListTodoResponse(BaseModel):
    message: str
    status: str
    todos: List[T]

class GetTodosResponse(ListTodoResponse):
    user_id: int