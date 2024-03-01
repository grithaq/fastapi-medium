from fastapi import APIRouter, status
from schema import SignUpSchema, SignUpResponse
from utils import has_pass
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