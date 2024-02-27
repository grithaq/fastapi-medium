from fastapi import APIRouter, status
from schema import TodoSchema, ListTodoResponse, TodoRequestSchema
import repositories


router = APIRouter()


@router.get(
        "/todo", status_code=status.HTTP_200_OK, tags=['TODO']
)
def get_todos():
    todos = repositories.todo.db_todo.get()
    todos = [t.__dict__ for t in todos]
    todos_schema = ListTodoResponse(
        message="Success", status=str(status.HTTP_200_OK), data=todos
    )
    return todos_schema


@router.post(
        "/todo", status_code=status.HTTP_201_CREATED, tags=['TODO']
)
def create_todo(todo: TodoRequestSchema):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.add(todo_obj)
    todos = [tr.__dict__ for tr in todos]
    list_todo_response = ListTodoResponse(
        message="Success", status=str(status.HTTP_201_CREATED),
        data=todos
    )
    return list_todo_response


@router.put(
    "/todo/{id}", status_code=status.HTTP_200_OK, tags=['TODO']
)
def update_todo(id: str, todo:TodoSchema):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.update(id, todo_obj)
    print(todos)
    