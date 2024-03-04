from .base import BaseModel, List, T, PaginationResponseModel
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
    categories: List[TodoCategorySchema]


class ListTodoResponse(BaseModel):
    message: str
    status: str
    todos: List[T]

class GetTodosResponse(BaseModel):
    message: str
    status: str
    user_id: int
    todos: List[T]
    pagination: PaginationResponseModel
    

class TodoResponse(BaseModel):
    message: str
    status: str

class TodoAddResponse(TodoResponse):
    todo: TodoRequestSchema