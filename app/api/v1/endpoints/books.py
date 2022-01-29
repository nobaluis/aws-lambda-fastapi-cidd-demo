from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_books():
    return [{"title": "hello"}, {"title:": "world"}]
