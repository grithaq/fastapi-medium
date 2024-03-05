from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture(scope="module")
def client() -> Generator:
    _application = create_app()
    with TestClient(_application) as _app:
        yield _app
