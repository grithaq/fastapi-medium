from fastapi import APIRouter, status
from schema import ListCategoryResponse
from repositories import db_categories


router = APIRouter()


@router.get(
        "/category", tags=["Categories"],
        response_model=ListCategoryResponse
        )
def get_categories():
    # print(db_categories.get_all_categories())
    categories = db_categories.get_all_categories()
    data = {
        "message": "Success",
        "status": str(status.HTTP_200_OK),
        "categories": categories
    }
    print(data)
    return data