from fastapi import APIRouter
import repositories

router = APIRouter()


@router.get("/category", tags=['Categories'])
def get_all_category():
    return repositories.db_categories.get_all_categories()