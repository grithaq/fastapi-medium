from fastapi import FastAPI, APIRouter
from routers import product

app = FastAPI()

router = APIRouter()

app.include_router(product.router, prefix="/api/v1/products")
