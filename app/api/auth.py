from fastapi import APIRouter
from schema import SignUpSchema

router = APIRouter()


@router.post('/sign_up', tags=["Auth"])
def sign_up(account: SignUpSchema):
    return account