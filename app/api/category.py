from fastapi import APIRouter, status
from schema import ListCategoryResponse, CategorySchema
from repositories import db_categories


router = APIRouter()


@router.get(
        "/category", tags=["Categories"],
        response_model=ListCategoryResponse,
        status_code=status.HTTP_200_OK
        )
def get_categories():
    categories = db_categories.get_all_categories()
    data = {
        "message": "Success",
        "status": str(status.HTTP_200_OK),
        "categories": categories
    }
    return data


@router.post(
    "/category", tags=["Categories"],
    response_model=ListCategoryResponse,
    status_code=status.HTTP_201_CREATED
    )
def add_category(category: CategorySchema):
    categories = db_categories.add_category(
        category.model_dump(exclude_unset=True)
        )
    data = {
        "message": "Success",
        "status": str(status.HTTP_200_OK),
        "categories": categories
    }
    return data


@router.delete(
    "/category/{id}", tags=["Categories"],
    response_model=ListCategoryResponse,
    status_code=status.HTTP_200_OK
)
def delete_category(id: str):
    categories = db_categories.delete_category(id)
    data = {
        "message": "Success",
        "status": str(status.HTTP_200_OK),
        "categories": categories
    }
    return data