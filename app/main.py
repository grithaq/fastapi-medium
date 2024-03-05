from api import auth, category, todo, user
from core.config import settings
from fastapi import FastAPI


def create_app():
    appplication = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
    )

    appplication.include_router(auth.router, prefix=settings.API_V1_STR)
    appplication.include_router(user.router, prefix=settings.API_V1_STR)
    appplication.include_router(category.router, prefix=settings.API_V1_STR)
    appplication.include_router(todo.router, prefix=settings.API_V1_STR)
    return appplication


app = create_app()
