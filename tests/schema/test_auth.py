from app.schema.auth import (MyProfileResponse, SignUpSchema, TokenData,
                             UserAuthSchema, UserInDb)


def test_sing_up_schema():
    data = {
        "id": "1",
        "username": "jhon",
        "email": "jhonmail",
        "password": "asdf",
    }
    schema = SignUpSchema(**data)
    assert schema
    assert schema.id == "1"
    assert schema.username == "jhon"
    assert schema.email == "jhonmail"
    assert schema.password == "asdf"


def test_token_data():
    data = {
        "username": "jhon",
    }
    schema = TokenData(**data)
    assert schema
    assert schema.username == "jhon"


def test_user_auth_schema():
    data = {
        "id": "1",
        "username": "Jhon",
        "email": "jhonmail",
        "disabled": False,
    }
    schema = UserAuthSchema(**data)
    assert schema
    assert schema.id == "1"
    assert schema.username == "Jhon"
    assert schema.email == "jhonmail"
    assert schema.disabled == False


def test_user_in_db():
    data = {
        "id": "1",
        "username": "Jhon",
        "email": "jhonmail",
        "disabled": False,
        "password": "asdf",
    }
    schema = UserInDb(**data)
    assert schema
    assert schema.password == "asdf"


def test_my_profile():
    data = {
        "message": "Success",
        "status": "200",
        "data": {"id": "1", "username": "Jhon", "email": "jhonmail", "disabled": False},
    }
    schema = MyProfileResponse(**data)
    assert schema
    assert schema.message == "Success"
    assert schema.status == "200"
    assert schema.data.id == "1"
    assert schema.data.username == "Jhon"
    assert schema.data.email == "jhonmail"
    assert schema.data.disabled == False
