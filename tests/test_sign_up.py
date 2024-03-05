from fastapi.testclient import TestClient
from core.config import settings
from app.main import create_app

application = create_app()
client = TestClient(application)


def test_sign_up():
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
