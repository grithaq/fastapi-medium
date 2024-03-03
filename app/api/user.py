import repositories
from fastapi import APIRouter, status, Depends
from schema import UserSchema, ListUserSchema, UserAuthSchema, MyProfileResponse
from core.error import NewError
from typing import Annotated
from utils import paginate, get_current_user


router = APIRouter()



@router.get('/profile', tags=['Profile'], status_code=status.HTTP_200_OK)
def get_profile(current_user: Annotated[UserAuthSchema, Depends(get_current_user)]):
    user = repositories.db_users.get_user_by_id(str(current_user.id))
    print(user.__dict__)
    user_schema = UserAuthSchema(
        id=user.id, username=user.username, email=user.email,
        disabled=user.disabled
    )
    return MyProfileResponse(
        message="Success", status=str(status.HTTP_200_OK), data=user_schema
    )


@router.put("/profile/{id}", tags=['Profile'], status_code=status.HTTP_200_OK)
def update_user(id: str, user: UserSchema):
    try:
        users = repositories.db_users.update(id, user.model_dump(exclude_unset=True))
        data = ListUserSchema(message="Success", status=str(status.HTTP_200_OK), data=users)
        return data
    except NewError:
        return NewError(status="404", msg="invalid user id, user with id {} not found".format(id))


@router.delete("/profile/{id}", tags=['Profile'], status_code=status.HTTP_200_OK)
def delete_user(id: str):
    try:
        users = repositories.db_users.delete(id)
        data = ListUserSchema(message="Success", status=str(status.HTTP_204_NO_CONTENT), data=users)
        return data
    except NewError:
        return NewError(status="404", msg="invalid user id, user with id {} not found".format(id))
        
