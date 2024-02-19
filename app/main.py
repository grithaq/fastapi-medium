from fastapi import FastAPI, APIRouter
from routers import product

app = FastAPI(
    title="Grithaq Product API",
    description="API for Grithaq Product",
    version="1.0.0",
)

router = APIRouter()

app.include_router(product.router, prefix="/api/v1/products")
