import repositories
from fastapi import APIRouter
from schema import UserSchema


router = APIRouter()


@router.get('/user', tags=['Users'])
def get_all_users():
    return repositories.db_users.get_users()
    

@router.post('/user', tags=['Users'])
def add_new_user(user: UserSchema):
    return repositories.db_users.add_user(user)


@router.put('/user/{id}', tags=['Users'])
def update_user(id: int, user: UserSchema):
    return repositories.db_users.update_user(id, user)