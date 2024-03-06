from core.config import settings
from fastapi.testclient import TestClient


def test_sign_up(client: TestClient):
    response = client.post(
        url=f"{settings.API_V1_STR}/sign_up",
        json={
            "id": "1",
            "username": "grithaq",
            "email": "gritmail",
            "password": "asdf",
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == 200


def test_login_for_token(client: TestClient):
    response = client.post(
        "http://localhost:8000/api/v1/sign_in",
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "",
            "username": "grithaq",
            "password": "asdf",
            "scope": "",
            "client_id": "",
            "client_secret": "",
        },
    )
    assert response.status_code == 200
