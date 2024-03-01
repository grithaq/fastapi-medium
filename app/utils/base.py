from passlib.context import CryptContext
from jose import jwt, JWSError
from typing import Union, Annotated
from datetime import timedelta, timezone, datetime
from core.config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def has_pass(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(repo, username: str):
    for r in repo:
        if username == r['username']:
            return r


def authenticate_user(repo, username: str, password: str):
    # get user from database
    user = get_user(repo, username)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update(
        {"exp": expire}
    )
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt

async def get_current_user():
    pass


async def get_current_active_user():
    pass

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    current = page
    total = len(items)
    data = {
        "current": current,
        "total": total,
        "items": items[start:end]
    }
    return data

