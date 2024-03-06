from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_todos(client: TestClient, get_token):
    response = client.get(
        url=f"{settings.API_V1_STR}/todo",
        params={"page": 1, "per_page": 10},
        headers={"accept": "application/json", "Authorization": get_token},
    )
    assert response.status_code == 200
    assert response.json() != {"detail": "Could not Validate"}


def test_create_todo(client: TestClient, get_token):
    todo_data = {
        "id": 1,
        "title": "Todo ke 1",
        "description": "Todo 1 desc",
        "categories": [{"id": 1, "name": "Learning"}, {"id": 4, "name": "Swiming"}],
    }
    response = client.post(
        url=f"{settings.API_V1_STR}/todo",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
            "Content-Type": "application/json",
        },
        json=todo_data,
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Success",
        "status": "201",
        "todo": {
            "id": 1,
            "title": "Todo ke 1",
            "description": "Todo 1 desc",
            "categories": [{"id": 1, "name": "Learning"}, {"id": 4, "name": "Swiming"}],
        },
    }


def test_update_todo(client: TestClient, get_token):
    response = client.put(
        url=f"{settings.API_V1_STR}/todo/1",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
            "Content-Type": "application/json",
        },
        json={
            "id": 1,
            "title": "Todo ke 2",
            "description": "Todo 2 desc",
            "categories": [{"id": 1, "name": "Learning"}],
        },
    )
    assert response.status_code == 200


def test_delete_todo(client: TestClient, get_token):
    response = client.delete(
        url=f"{settings.API_V1_STR}/todo/1",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 200
