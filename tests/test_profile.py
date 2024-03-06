import json as js

from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_profile(client: TestClient, get_token):
    response = client.get(
        url=f"{settings.API_V1_STR}/profile",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
        },
    )
    assert response.status_code == 200


def test_update_profile(client: TestClient, get_token):
    response = client.put(
        url=f"{settings.API_V1_STR}/profile",
        headers={
            "accept": "application/json",
            "Authorization": get_token,
            "Content-Type": "application/json",
        },
        data=js.dumps(
            {"id": "1", "username": "jhon", "email": "jhonmail", "disabled": True}
        ),
    )
    assert response.status_code == 200
