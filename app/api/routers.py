from fastapi import APIRouter

from app.api.endpoints import memes_router

main_router = APIRouter()
main_router.include_router(
    memes_router,
    prefix='/memes',
    tags=['memes']
)
