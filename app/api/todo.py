from fastapi import APIRouter, status
from schema import TodoSchema, ListTodoResponse
import repositories


router = APIRouter()


@router.post(
        "/todo", status_code=status.HTTP_201_CREATED, tags=['TODO']
)
def create_todo(todo: TodoSchema):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.add(todo_obj)
    todos = [tr.__dict__ for tr in todos]
    list_todo_response = ListTodoResponse(
        message="Success", status=str(status.HTTP_201_CREATED),
        data=todos
    )
    return list_todo_response