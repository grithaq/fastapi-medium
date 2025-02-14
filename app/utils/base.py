from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

from core.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from schema import TokenData, UserAuthSchema, UserInDb

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/sign_in")


def get_db():
    from repositories import db_users

    return db_users.get()


def has_pass(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(repo, username: str):
    for r in repo:
        if username == r.username:
            user_in_db = UserInDb(
                id=r.id,
                username=r.username,
                email=r.email,
                password=r.password,
                disabled=r.disabled,
            )
            return user_in_db


def authenticate_user(repo, username: str, password: str):
    # get user from database
    user = get_user(get_db(), username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encode_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    creadential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate",
        headers={"WWW-Authenticate": "Barrer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise creadential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise creadential_exception
    user = get_user(get_db(), username=token_data.username)
    if user is None:
        raise creadential_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserAuthSchema, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    current = page
    total = len(items)
    data = {"current": current, "total": total, "items": items[start:end]}
    return data
