from typing import Annotated

import repositories
from core.error import NewError
from fastapi import APIRouter, Depends, status
from schema import ListUserSchema, MyProfileResponse, UserAuthSchema
from utils import get_current_user

router = APIRouter()


@router.get("/profile", tags=["Profile"], status_code=status.HTTP_200_OK)
def get_profile(current_user: Annotated[UserAuthSchema, Depends(get_current_user)]):
    user = repositories.db_users.get_user_by_id(str(current_user.id))
    user_schema = UserAuthSchema(
        id=user.id, username=user.username, email=user.email, disabled=user.disabled
    )
    return MyProfileResponse(
        message="Success", status=str(status.HTTP_200_OK), data=user_schema
    )


@router.put("/profile/", tags=["Profile"], status_code=status.HTTP_200_OK)
def update_profile(
    user: UserAuthSchema,
    current_user: Annotated[UserAuthSchema, Depends(get_current_user)],
):
    try:
        users = repositories.db_users.update(
            str(current_user.id), user.model_dump(exclude_unset=True)
        )
        print(users)
        user_schema = UserAuthSchema(
            id=users.id,
            username=users.username,
            email=users.email,
            disabled=users.disabled,
        )
        return MyProfileResponse(
            message="Success", status=str(status.HTTP_200_OK), data=user_schema
        )
    except NewError:
        return NewError(
            status="404", msg="invalid user id, user with id {} not found".format(id)
        )


@router.delete("/profile/{id}", tags=["Profile"], status_code=status.HTTP_200_OK)
def delete_profile(id: str):
    try:
        users = repositories.db_users.delete(id)
        data = ListUserSchema(
            message="Success", status=str(status.HTTP_204_NO_CONTENT), data=users
        )
        return data
    except NewError:
        return NewError(
            status="404", msg="invalid user id, user with id {} not found".format(id)
        )
