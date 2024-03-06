from app.core.config import settings
from fastapi.testclient import TestClient
from tests.conftest import get_token



def test_get_categories(client: TestClient, get_token):    
    response = client.get(
        url=f"{settings.API_V1_STR}/categories",
        params={
            "page": 1,
            "per_page": 10
        },
        headers={
            'accept': "application/json",
            "Authorization": get_token
        }
    )
    response.status_code == 200