import repositories
from fastapi import APIRouter


router = APIRouter()


@router.get('/user')
def get_all_users():
    return repositories.db_users.get_users()
    


