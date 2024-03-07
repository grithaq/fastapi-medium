from app.schema.user import (AccountSchema, ListUserResponse, SignInResponse,
                             SignUpResponse, UserSchema)


def test_user_schema():
    data = {"id": 1, "username": "Jhon"}
    schema = UserSchema(**data)
    assert schema
    assert schema.id == 1
    assert schema.username == "Jhon"


def test_list_user_response_schema():
    data = {
        "message": "Success",
        "status": "200",
        "data": [],
        "pagination": {"current": 1, "total": 0},
    }
    schema = ListUserResponse(**data)
    assert schema
    assert schema.pagination.current == 1
    assert schema.pagination.total == 0


def test_account_schema():
    account_data = {
        "id": "1",
        "username": "Jhon",
        "email": "jhonmail",
    }
    account_schema = AccountSchema(**account_data)

    assert account_schema
    assert account_schema.id == "1"


def test_signup_response():
    account_data = {
        "id": "1",
        "username": "Jhon",
        "email": "jhonmail",
    }
    account_schema = AccountSchema(**account_data)
    data = {"message": "Success", "status": "200", "account": account_schema}
    schema = SignUpResponse(**data)
    assert schema
    assert schema.account.id == "1"


def test_sign_in_response():
    data = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJncml0aGFxIiwiZXhwIjoxNzA5ODA4MjE2fQ.SFAxzUO2z4zh-pF7Ggt_--HBEkYvzitv_PWMrU6q4HQ",
        "token_type": "bearer",
    }
    schema = SignInResponse(**data)
    assert schema
    assert (
        schema.access_token
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJncml0aGFxIiwiZXhwIjoxNzA5ODA4MjE2fQ.SFAxzUO2z4zh-pF7Ggt_--HBEkYvzitv_PWMrU6q4HQ"
    )
