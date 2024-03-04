from fastapi import APIRouter, status, Depends
from schema import ListTodoResponse, TodoRequestSchema, GetTodosResponse, TodoResponse, UserAuthSchema, ResponseModel
import repositories
from core.error import NewError
from utils import paginate, get_current_user
from typing import Annotated


router = APIRouter()


@router.get(
        "/todo", status_code=status.HTTP_200_OK, tags=['TODO'],
)
def get_todos(
    page: int, per_page: int, current_user: Annotated[UserAuthSchema, Depends(get_current_user)]
):
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
    todos = paginate(todos, page, per_page)
    pgsn = {
        "current": todos['current'],
        "total": todos['total']
    }
    todos_schema = GetTodosResponse(
        message="Success", status=str(status.HTTP_200_OK),
        todos=todos['items'], user_id=1, pagination=pgsn
    )
    return todos_schema


@router.post(
        "/todo", status_code=status.HTTP_201_CREATED, tags=['TODO']
)
def create_todo(
    todo: TodoRequestSchema
):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.add(1, todo_obj)
    todos = [tr.__dict__ for tr in todos]
    list_todo_response = ListTodoResponse(
        message="Success", status=str(status.HTTP_201_CREATED),
        todos=todos
    )
    return list_todo_response


@router.put(
    "/todo/{id}", status_code=status.HTTP_200_OK, tags=['TODO']
)
def update_todo(
    id: str, todo:TodoRequestSchema, current_user: Annotated[UserAuthSchema, Depends(get_current_user)]
):
    todo_obj = todo.model_dump(exclude_unset=True)
    todos = repositories.todo.db_todo.update(int(id), current_user.id, todo_obj)
    todo_schema = TodoRequestSchema(
        id=todos.id, title=todos.title, description=todos.description,
        categories=todos.categories
    )
    todo_response = ResponseModel(
        message="Success", status=str(status.HTTP_200_OK),
        data=[todo_schema]
    )
    return todo_response
    

@router.delete(
    "/todo/{id}", tags=['TODO']
)
def delete_todo(
    id: str, current_user: Annotated[UserAuthSchema, Depends(get_current_user)]
):
    todo = repositories.todo.db_todo.delete(id)
    print(todo)
    if todo != None:
        data = TodoResponse(
            message="Success", status=str(status.HTTP_204_NO_CONTENT)
        )
        return data
    return NewError(status="404", msg="invalid todo id, todo with id {} not found".format(id))