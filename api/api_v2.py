from fastapi import APIRouter
from endpoints import generation


api_router = APIRouter()
api_router.include_router(generation.router, prefix="/api", tags=["answers"])