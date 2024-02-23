from fastapi import APIRouter, status
from schema import TodoSchema, ListTodoResponse
import repositories


router = APIRouter()


@router.post(
        "/todo", status_code=status.HTTP_201_CREATED, tags=['TODO']
)
def create_todo(todo: TodoSchema):
    # print(todo.model_dump(exclude_unset=True))
    todo_repo = repositories.db_todo.add(todo.model_dump(exclude_unset=True))
    print(type(todo_repo), todo_repo)
    print(type(todo_repo), todo_repo)
    list_todo_response = ListTodoResponse(
        message="Success", status=str(status.HTTP_201_CREATED), data=todo_repo
    )
    return list_todo_response