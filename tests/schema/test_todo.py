from app.schema.todo import (ListTodoResponse, TodoCategorySchema,
                             TodoRequestSchema, TodoSchema)


def test_todo_schema():
    category = TodoCategorySchema(id=1, name="Learning")
    data = {
        "id": 1,
        "title": "Learning Fastapi",
        "description": "Learning Fastapi Medium Level",
        "categories": [category],
        "user": {"id": 1, "username": "grithaq"},
    }
    schema = TodoSchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.title == "Learning Fastapi"
    assert schema.description == "Learning Fastapi Medium Level"
    assert schema.user.id == 1
    assert schema.user.username == "grithaq"
    assert schema.categories[0].id == 1
    assert schema.categories[0].name == "Learning"


def test_todo_request_schema():
    data = {
        "id": 1,
        "title": "Learning Fastapi",
        "description": "Learning Fastapi Medium Level",
        "categories": [
            {
                "id": 1,
                "name": "Learning",
            }
        ],
    }
    schema = TodoRequestSchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.title == "Learning Fastapi"
    assert schema.description == "Learning Fastapi Medium Level"
    assert schema.categories[0].id == 1
    assert schema.categories[0].name == "Learning"


def test_list_todo_reponse():
    data = {
        "message": "Success",
        "status": "200",
        "todos": [
            {
                "id": 1,
                "title": "Learning Fastapi",
                "description": "Learning Fastapi Medium Level",
                "categories": [
                    {
                        "id": 1,
                        "name": "Learning",
                    }
                ],
            }
        ],
    }
    schema = ListTodoResponse(**data)
    assert schema.message == "Success"
    assert schema.todos[0]["id"] == 1
