from fastapi import APIRouter

from .endpoints import books

router = APIRouter()

router.include_router(books.router, prefix="/books", tags=["Books"])
