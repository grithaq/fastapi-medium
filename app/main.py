from fastapi import FastAPI, APIRouter
from routers import product, user, category

app = FastAPI(
    title="Grithaq Product API",
    description="API for Grithaq Product",
    version="1.0.0",
)

router = APIRouter()

app.include_router(product.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
