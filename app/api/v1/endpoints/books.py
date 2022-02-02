from fastapi import APIRouter

from ..service import books_service as books

router = APIRouter()


@router.get("/")
async def get_books():
    return [{"title": "hello"}, {"title:": "world"}]


@router.get("/by-author/{author}")
async def get_books_by_author(author: str):
    return books.get_books_by_author(author)


@router.get("/by-author/{author}/by-title/{title}")
async def get_book(author: str, title: str):
    return books.get_book(title, author)
