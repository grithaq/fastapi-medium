import db_on_mem
from fastapi import APIRouter

router = APIRouter()


@router.get('/products')
def get_products():
    return db_on_mem.db_products.get_products()