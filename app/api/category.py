from typing import Annotated

from fastapi import APIRouter, Depends, status
from repositories import db_categories
from schema import (CategoriesResponse, CategoryRequestSchema, CategorySchema,
                    ListCategoryResponse, UserAuthSchema)
from utils.base import get_current_user, paginate

router = APIRouter()


@router.get("/category", tags=["Categories"], status_code=status.HTTP_200_OK)
def get_categories(
    page: int,
    per_page: int,
    current_user: Annotated[UserAuthSchema, Depends(get_current_user)],
):
    categories = db_categories.get()
    categories = paginate(categories, page, per_page)
    pgsn = {"current": categories["current"], "total": categories["total"]}
    list_category_response = CategoriesResponse(
        message="Success",
        status=str(status.HTTP_200_OK),
        data=categories["items"],
        pagination=pgsn,
        user_id=current_user.id,
    )
    return list_category_response


@router.post("/category", tags=["Categories"], status_code=status.HTTP_201_CREATED)
def add_category(
    category: CategoryRequestSchema,
    current_user: Annotated[UserAuthSchema, Depends(get_current_user)],
):
    categories = db_categories.add(
        current_user.id, category.model_dump(exclude_unset=True)
    )
    list_category_response = ListCategoryResponse(
        message="Success",
        status=str(status.HTTP_201_CREATED),
        data=categories,
        user_id=current_user.id,
    )
    return list_category_response


@router.put("/category/{id}", tags=["Categories"], status_code=status.HTTP_200_OK)
def update_category(
    id: str,
    category: CategorySchema,
    current_user: Annotated[UserAuthSchema, Depends(get_current_user)],
):
    categories = db_categories.update(
        int(current_user.id), id, category.model_dump(exclude_unset=True)
    )
    print(categories)
    list_category_response = ListCategoryResponse(
        message="Success",
        status=str(status.HTTP_200_OK),
        data=categories,
        user_id=current_user.id,
    )
    return list_category_response


@router.delete(
    "/category/{id}", tags=["Categories"], status_code=status.HTTP_404_NOT_FOUND
)
def delete_category(
    id: str, curren_user: Annotated[UserAuthSchema, Depends(get_current_user)]
):
    category = db_categories.delete(id)
    try:
        list_category_response = ListCategoryResponse(
            message="Success",
            status=str(status.HTTP_200_OK),
            data=category,
            user_id=curren_user.id,
        )
        return list_category_response
    except Exception:
        list_category_response = ListCategoryResponse(
            message=category,
            status=str(status.HTTP_404_NOT_FOUND),
            data=[],
            user_id=curren_user.id,
        )
        return list_category_response
