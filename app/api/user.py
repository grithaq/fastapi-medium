import repositories
from fastapi import APIRouter, status
from schema import UserSchema, ListUserSchema, PaginationResponseModel
from core.error import NewError


router = APIRouter()


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

@router.get('/user', tags=['Users'], status_code=status.HTTP_200_OK)
def get_all_users(per_page: int = 10, page: int = 1):
    users = repositories.db_users.get()
    users = paginate(users, page, per_page)
    pgsn = {
        "current": users['current'],
        "total": users['total']
    }
    lus = ListUserSchema(message="Success", status=str(status.HTTP_200_OK), data=users['items'], pagination=pgsn)
    return lus
    

@router.post('/user', tags=['Users'], status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):
    users = repositories.db_users.add(user.model_dump(exclude_unset=True))
    lus = ListUserSchema(message="Success", status=str(status.HTTP_201_CREATED), data=users)
    return lus


@router.put("/user/{id}", tags=['Users'], status_code=status.HTTP_200_OK)
def update_user(id: str, user: UserSchema):
    try:
        users = repositories.db_users.update(id, user.model_dump(exclude_unset=True))
        data = ListUserSchema(message="Success", status=str(status.HTTP_200_OK), data=users)
        return data
    except NewError:
        return NewError(status="404", msg="invalid user id, user with id {} not found".format(id))


@router.delete("/user/{id}", tags=['Users'], status_code=status.HTTP_200_OK)
def delete_user(id: str):
    try:
        users = repositories.db_users.delete(id)
        data = ListUserSchema(message="Success", status=str(status.HTTP_204_NO_CONTENT), data=users)
        return data
    except NewError:
        return NewError(status="404", msg="invalid user id, user with id {} not found".format(id))
        
