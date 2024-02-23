from fastapi import APIRouter, status
from schema import ListCategoryResponse, CategorySchema
from repositories import db_categories


router = APIRouter()


@router.get(
        "/category", tags=["Categories"], status_code=status.HTTP_200_OK
)
def get_categories():
    categories = db_categories.get()
    list_category_response = ListCategoryResponse(
        message="Success", status=str(status.HTTP_200_OK), data=categories
    )
    return list_category_response


@router.post(
        "/category", tags=["Categories"], status_code=status.HTTP_201_CREATED
)
def add_category(category: CategorySchema):
    categories = db_categories.add(category.model_dump(exclude_unset=True))
    list_category_response = ListCategoryResponse(
        message="Success", status=str(status.HTTP_201_CREATED), data=categories
    )
    return list_category_response


@router.put(
        "/category/{id}", tags=["Categories"], status_code=status.HTTP_200_OK
)
def update_category(id: str, category: CategorySchema):
    categories = db_categories.update(
        id, category.model_dump(exclude_unset=True)
    )
    list_category_response = ListCategoryResponse(
        message="Success", status=str(status.HTTP_200_OK), data=categories
    )
    return list_category_response


@router.delete(
        "/category/{id}", tags=["Categories"], status_code=status.HTTP_404_NOT_FOUND
)
def delete_category(id: str):
    print("DELETE")
    category = db_categories.delete(id)
    print(category)
    try:
        list_category_response = ListCategoryResponse(
            message="Success", status=str(status.HTTP_200_OK), data=category
        )
        return list_category_response
    except Exception:
        list_category_response = ListCategoryResponse(
            message=category, status=str(status.HTTP_404_NOT_FOUND), data=[]
        )
        return list_category_response
