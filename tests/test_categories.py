from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_category(client: TestClient, get_token):
    response = client.get(
        url=f"{settings.API_V1_STR}/category",
        params={"page": 1, "per_page": 10},
        headers={"accept": "application/json", "Authorization": get_token},
    )
    assert response.status_code == 200
    assert response.json() != {"detail": "Could not Validate"}
    assert response.json() == {
        "message": "Success",
        "status": "200",
        "data": [],
        "user_id": 1,
        "pagination": {"current": 1, "total": 0},
    }


def test_createa_category(client: TestClient, get_token):
    category_data = {"id": 1, "name": "Learning"}
    response = client.post(
        url=f"{settings.API_V1_STR}/category",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
            "Content-Type": "application/json",
        },
        json=category_data,
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Success",
        "status": "201",
        "data": [{"id": 1, "name": "Learning", "user_id": 1}],
        "user_id": 1,
    }


# def test_update_category(client: TestClient, get_token):
#     category_data = {"id": 1, "name": "Shoping"}
#     response = client.put(
#         url=f"{settings.API_V1_STR}/category/1",
#         headers={
#             "accept": "application/json",
#             "Authorization": get_token,
#             "Content-Type": "application/json",
#         },
#         json=category_data,
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "message": "Success",
#         "status": "200",
#         "data": [{"id": 1, "name": "Shoping"}],
#         "user_id": 1,
#     }


# def test_delete_category(client: TestClient, get_token):
#     response = client.delete(
#         url=f"{settings.API_V1_STR}/category/1",
#         headers={
#             "accept": "application/json",
#             "Authorization": get_token,
#             "Content-Type": "application/json",
#         },
#     )
#     assert response.status_code == 404
#     assert response.json() == {
#         "message": "Success",
#         "status": "200",
#         "data": [],
#         "user_id": 1,
#     }
