from fastapi import FastAPI, APIRouter
from api import todo, user, category

app = FastAPI(
    title="Grithaq TODO API",
    description="API for Grithaq TODO App",
    version="1.0.0",
)

router = APIRouter()

app.include_router(todo.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
