from app.schema.category import (CategoriesResponse, CategoryRequestSchema,
                                 CategorySchema, ListCategoryResponse,
                                 TodoCategorySchema)


def test_category_schema():
    data = {
        "id": 1,
        "name": "Learning",
    }
    schema = CategorySchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.name == "Learning"


def test_category_request_schema():
    data = {
        "id": 1,
        "name": "Learning",
    }
    schema = CategoryRequestSchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.name == "Learning"


def test_list_category_response():
    data = {"message": "Success", "status": "200", "user_id": 1, "data": []}
    schema = ListCategoryResponse(**data)
    assert schema
    assert schema.user_id == 1


def test_todo_category_schema():
    data = {
        "id": 1,
        "name": "Learning",
    }
    schema = TodoCategorySchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.name == "Learning"


def test_category_response():
    data = {
        "message": "Success",
        "status": "200",
        "pagination": {
            "total": 1,
            "page": 1,
            "pages": 1,
            "per_page": 10,
        },
        "user_id": 1,
        "data": [
            {
                "id": 1,
                "name": "Learning",
            }
        ],
    }
    schema = CategoriesResponse(**data)
    assert schema
    assert schema.user_id == 1

    assert schema.pagination
    assert schema.pagination.total == 1
    assert schema.pagination.page == 1
    assert schema.pagination.pages == 1
    assert schema.pagination.per_page == 10
