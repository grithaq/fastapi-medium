from typing import List, TypeVar
from dataclasses import dataclass

T = TypeVar("T")


class User:
    id: int
    name: str

    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Category:
    id: int
    name: str
    user: User

    def __init__(self, id: int = None, name: str = None, user: User = None):
        self.id = id
        self.name = name
        self.user = user

    def __repr__(self) -> str:
        return self.name


class Todo:
    id: int
    title: str
    description: str
    categories: List[Category]
    user: User

    def __init__(self, id: int = None, title: str = None, description: str = None, categories: List[Category] = None, user: User = None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.categories = categories
        self.user = user
    
    def __repr__(self) -> str:
        self.title
