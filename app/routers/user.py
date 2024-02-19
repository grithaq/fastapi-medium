import repositories
from fastapi import APIRouter
from schema import UserSchema


router = APIRouter()


@router.get('/user', tags=['Users'])
async def get_all_users():
    return repositories.db_users.get_users()


@router.post('/user', tags=['Users'])
async def add_new_user(user: UserSchema):
    return repositories.db_users.add_user(user)


@router.put('/user/{id}', tags=['Users'])
async def update_user(id: int, user: UserSchema):
    return repositories.db_users.update_user(id, user)


@router.delete('/user/{id}', tags=['Users'])
async def delete_user(id: int):
    return repositories.db_users.delete_user(id)