from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/test")
def test():
    return {"message": "Test message"}

app.include_router(router, prefix="/api")
