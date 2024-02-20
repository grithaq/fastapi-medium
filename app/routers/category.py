from fastapi import APIRouter
from schema import CategorySchema
import repositories

router = APIRouter()


@router.get("/category", tags=['Categories'])
def get_all_category():
    return repositories.db_categories.get_all_categories()


@router.post("/category", tags=['Categories'])
def add_new_category(category: CategorySchema):
    return repositories.db_categories.add_category(category)


@router.put("/category/{id}", tags=['Categories'])
def update_category(id: str, category: CategorySchema):
    return repositories.db_categories.update_category(id, category)

