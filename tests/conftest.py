import pytest

from app.main import create_app


@pytest.fixture
def app():
    _app = create_app()
    with _app.app_context():
        yield _app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


def test_ku():
    assert 1 == 1