from fastapi import APIRouter, status
from schema import TodoSchema


router = APIRouter()


@router.post(
        "/todo", status_code=status.HTTP_201_CREATED, tags=['TODO']
)
def create_todo(todo: TodoSchema):
    print(todo)