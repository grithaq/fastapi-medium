import db_on_mem
from fastapi import APIRouter
from schema import Product
from fastapi.openapi.docs import get_swagger_ui_html

router = APIRouter()


@router.get('/product', tags=['Products'], summary="Get Products Endpoint")
async def get_products():
    """Get all products Endpoint

    Return: Return all products from memory
    """
    
    return db_on_mem.db_products.get_products()


@router.post('/product', summary="Create Product Endpoint", tags=['Products'])
async def create_product(product: Product):
    """Create Product
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return db_on_mem.db_products.add_product(product)


@router.put('/product/{id}' ,tags=['Products'])
async def update_product(prod_id: str, product: Product):
    return db_on_mem.db_products.update_product(prod_id, product)

@router.delete('product/{id}', tags=['Products'])
async def delete_product(prod_id: str):
    return db_on_mem.db_products.delete_product(prod_id)

@router.get("/custom-docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        title="Custom Docs",
        url="/openapi.json",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )