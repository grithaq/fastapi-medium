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
