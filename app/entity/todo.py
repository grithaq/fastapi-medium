from typing import List

from .base import T
from .user import User


class Todo:
    id: int
    title: str
    description: str
    categories: List[T]
    user: User
    user_id: int
