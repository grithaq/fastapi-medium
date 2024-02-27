from .user import User
from .todo import Todo
from typing import List


class Category:
    id: int
    name: str
    user: User
    todos: List[Todo]
    user_id: int
    todo_id: int
