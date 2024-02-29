from fastapi import APIRouter, status
from schema import ListCategoryResponse, CategorySchema, CategoryRequestSchema, CategoriesResponse
from repositories import db_categories
from utils.base import paginate


router = APIRouter()


@router.get(
        "/category", tags=["Categories"], status_code=status.HTTP_200_OK
)
def get_categories(page: int = 1, per_page: int = 10):
    categories = db_categories.get()
    categories = paginate(categories, page, per_page)
    pgsn = {
        "current": categories['current'],
        "total": categories['total']
    }
    list_category_response = CategoriesResponse(
        message="Success", status=str(status.HTTP_200_OK), data=categories['items'],
        pagination=pgsn
    )
    return list_category_response


@router.post(
        "/category", tags=["Categories"], status_code=status.HTTP_201_CREATED
)
def add_category(category: CategoryRequestSchema):
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
