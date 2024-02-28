from fastapi import APIRouter, status
from schema import TodoSchema, ListTodoResponse, TodoRequestSchema, GetTodosResponse
import repositories


router = APIRouter()


@router.get(
        "/todo", status_code=status.HTTP_200_OK, tags=['TODO']
)
def get_todos():
    todos = repositories.todo.db_todo.get()

    list_todo = []
    todos = [t.__dict__ for t in todos]
    for t in todos:
        if t['user_id'] == 1:
            todo = {
                "id": t['id'],
                "title": t['title'],
                "description": t['description'],
                "categories": t['categories'],
            }
            list_todo.append(todo)
    todos_schema = GetTodosResponse(
        message="Success", status=str(status.HTTP_200_OK),
        todos=list_todo, user_id=1
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
        todos=todos
    )
    return list_todo_response


@router.put(
    "/todo/{id}", status_code=status.HTTP_200_OK, tags=['TODO']
)
def update_todo(id: str, todo:TodoRequestSchema):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.update(id, todo_obj)
    todos = [tr.__dict__ for tr in todos]
    list_todo_response = ListTodoResponse(
        message="Success", status=str(status.HTTP_200_OK),
        todos=todos
    )
    return list_todo_response
    