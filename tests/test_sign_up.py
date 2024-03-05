import httpx


def test_sign_up():
    r = httpx.post(
        url="http://localhost:8000/api/v1/sign_up",
        json={
            "id": "1",
            "username": "grithaq",
            "email": "gritmail",
            "password": "asdf",
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )

    assert r.status_code == 200
    assert r.json() == {
        "message": "Success",
        "status": "201",
        "account": {"id": "1", "username": "grithaq", "email": "gritmail"},
    }
