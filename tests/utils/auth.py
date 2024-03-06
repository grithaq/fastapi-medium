from fastapi.testclient import TestClient
from app.core.config import settings


def sign_up_user(client: TestClient):
    new_user = {
        "id": "1",
        "username": "grithaq",
        "email": "grimail",
        "password": "asdf",
    }
    response = client.post(
        url=f"{settings.API_V1_STR}/sign_up",
        json=new_user,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    

def get_user_token(client: TestClient):
    sign_up_user(client)
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
    response_data = response.json()
    token = f"Bearer {response_data['access_token']}"
    return token


