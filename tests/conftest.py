from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from tests.utils.auth import get_user_token


@pytest.fixture(scope="module")
def client() -> Generator:
    _application = create_app()
    with TestClient(_application) as _app:
        yield _app


@pytest.fixture(scope="module")
def get_token(client):
    yield get_user_token(client)
