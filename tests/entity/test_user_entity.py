from app.entity.user import User


def test_entity_user():
    user = User()
    user.id = 1
    user.username = "jhon"
    user.email = "jhonmail"
    user.password = "asdf"
    user.disabled = False
    assert user
    assert user.username == "jhon"
    assert user.email == "jhonmail"
    assert user.password == "asdf"
    assert user.disabled == False
