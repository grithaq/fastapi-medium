from fastapi import APIRouter, status, HTTPException, Depends
from schema import SignUpSchema, SignUpResponse, SignInResponse, UserAuthSchema
from utils import has_pass, authenticate_user, create_access_token, get_current_user, get_current_active_user
from fastapi.security import OAuth2PasswordRequestForm
from core.config import settings
from datetime import timedelta
from typing import Annotated
import repositories

router = APIRouter()


@router.post('/sign_up', tags=["Auth"])
def sign_up(account: SignUpSchema):
    account.password = has_pass(account.password)
    # print(account.model_dump(exclude_unset=True))
    new_account = repositories.db_users.add(account.model_dump(exclude_unset=True))
    print(new_account)
    account = {
        'id': new_account.id,
        'username': new_account.username,
        'email': new_account.email
    }
    print(account)
    return SignUpResponse(
        message="Success", status=str(status.HTTP_201_CREATED), account=account
    )


@router.post(
    "/sign_in", tags=['Auth'], status_code=status.HTTP_200_OK
)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(repositories.db_users.get(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return SignInResponse(
        access_token=access_token, token_type="bearer"
    )


@router.get(
    '/account/me', tags=['Auth'], status_code=status.HTTP_200_OK,
    response_model=SignUpSchema
)
def get_me(
    current_user: Annotated[SignUpSchema, Depends(get_current_user)]
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[UserAuthSchema, Depends(get_current_active_user)]
):
    print(f"auth endpoint : {current_user}")
    return [{"item_id": "Foo", "owner": current_user.username}]