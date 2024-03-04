from typing import List

from .todo import Todo
from .user import User


class Category:
    id: int
    name: str
    user: User
    todos: List[Todo]
    user_id: int
    todo_id: int
