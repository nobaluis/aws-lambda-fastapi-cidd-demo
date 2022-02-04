from fastapi import APIRouter

from ..model.book import Book
from ..service import books_service as books

router = APIRouter()


@router.get("/")
async def get_books():
    return [{"title": "hello"}, {"title:": "world"}]


@router.post("/")
async def post_book(book: Book):
    books.create_book(book)


@router.put("/")
async def put_book(book: Book):
    return books.update_book(book)


@router.get("/by-author/{author}")
async def get_books_by_author(author: str):
    return books.get_books_by_author(author)


@router.get("/by-author/{author}/by-title/{title}")
async def get_book(author: str, title: str):
    return books.get_book(title, author)


@router.delete("/by-author/{author}/by-title/{title}")
async def delete_book(author: str, title: str):
    books.delete_book(title, author)
