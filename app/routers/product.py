import app.repositories as repositories
from fastapi import APIRouter
from schema import Product


router = APIRouter()


@router.get('/product', tags=['Products'], summary="Get Products Endpoint")
async def get_products():
    """Get all products Endpoint

    Return: Return all products from memory
    """
    
    return repositories.db_products.get_products()


@router.post('/product', summary="Create Product Endpoint", tags=['Products'])
async def create_product(product: Product):
    """Create Product    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return repositories.db_products.add_product(product)


@router.put('/product/{id}', tags=['Products'])
async def update_product(prod_id: str, product: Product):
    return repositories.db_products.update_product(prod_id, product)


@router.delete('product/{id}', tags=['Products'])
async def delete_product(prod_id: str):
    return repositories.db_products.delete_product(prod_id)
