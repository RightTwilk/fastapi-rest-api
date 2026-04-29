from fastapi import APIRouter, Depends, HTTPException, status
from app.items.schemas import (
    BookBase,
    BookCreate,
)
from app.items.services import create_book, get_book, get_book_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import session_maker
from app.items.models import Book

item_router = APIRouter(tags=["Items"], prefix="/item")


# book views
book_router = APIRouter(tags=["Book"], prefix="/book")


@book_router.post("create_book/", response_model=BookCreate)
async def create_book_view(
    book: BookCreate, session: AsyncSession = Depends(session_maker)
):
    await create_book(session=session, book_data=book)
    return {"BookCreate": "Succes"}


@book_router.get("get_book/", response_model=list[Book])
async def get_book_view(
    book: BookBase, session: AsyncSession = Depends(session_maker)
) -> list[Book]:
    return await get_book(session=session)


@book_router.get("get_book_by_id/{book_id}", response_model=BookBase | None)
async def get_book_by_id_view(
    book_id: int, session: AsyncSession = Depends(session_maker)
) -> BookBase | None:
    book = await get_book_by_id(session=session, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return None

    return BookBase.model_validate(book)
