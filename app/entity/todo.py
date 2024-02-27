from .base import List
from .category import Category
from .user import User


class Todo:
    id: int
    title: str
    description: str
    categories: List[Category]
    user: User
    user_id: int