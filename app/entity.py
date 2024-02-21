from typing import List, TypeVar
from dataclasses import dataclass

T = TypeVar("T")

class User:
    id: int
    name: str
    

class Category:
    id: int
    name: str
    user: User


class Todo:
    id: int
    title: str
    description: str
    categories: List[Category]
    user: User
