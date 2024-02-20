from fastapi import APIRouter
from schema import TodoSchema

router = APIRouter()


@router.get("/category")
def get_all_category(todo: TodoSchema):
    return todo