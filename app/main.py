from api import auth, category, todo, user
from core.config import settings
from fastapi import APIRouter, FastAPI

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG,
)

router = APIRouter()

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(user.router, prefix=settings.API_V1_STR)
app.include_router(category.router, prefix=settings.API_V1_STR)
app.include_router(todo.router, prefix=settings.API_V1_STR)
