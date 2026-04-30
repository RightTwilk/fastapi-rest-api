from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from app.items.models import Book, Magazine, Newspaper
from app.items.schemas import (
    BookCreate,
    MagazineCreate,
    NewspaperCreate,
    BookResponse,
    MagazineResponse,
)
from typing import Optional


# books
async def get_book(session: AsyncSession) -> list[BookResponse]:
    result: Result[tuple[Book]] = await session.execute(select(Book).order_by(Book.id))
    return [BookResponse.model_validate(b) for b in result.scalars().all()]


async def get_book_by_id(session: AsyncSession, book_id: int) -> Optional[Book]:
    return await session.get(Book, book_id)


async def create_book(session: AsyncSession, book_data: BookCreate) -> BookResponse:
    book_model = Book(**book_data.model_dump())
    session.add(book_model)
    await session.commit()
    await session.refresh(book_model)
    return BookResponse.model_validate(book_model)


# magazines
async def create_magazine(
    session: AsyncSession, magazine_data: MagazineCreate
) -> MagazineResponse:
    magazine = Magazine(**magazine_data.model_dump())
    session.add(magazine)
    await session.commit()
    await session.refresh(magazine)
    return MagazineResponse.model_validate(magazine)


async def get_magazine(session: AsyncSession) -> list[MagazineResponse]:
    result: Result[tuple[Magazine]] = await session.execute(
        select(Magazine).order_by(Magazine.id)
    )
    return [MagazineResponse.model_validate(b) for b in result.scalars().all()]


async def get_magazine_by_id(
    session: AsyncSession, magazine_id: int
) -> Optional[Magazine]:
    return await session.get(Magazine, magazine_id)


# newspaper
async def create_newspaper(session: AsyncSession, newspaper_data: NewspaperCreate):
    newspaper = Newspaper(**newspaper_data.model_dump())
    session.add(newspaper)
    await session.commit()
    await session.refresh(newspaper)
    return {"Newspaper": "Created"}


async def get_newspaper_by_id(
    session: AsyncSession, newspaper_id: int
) -> Optional[Newspaper]:
    return await session.get(Newspaper, newspaper_id)


async def get_newspaper(session: AsyncSession) -> list[Newspaper]:
    result: Result[tuple[Newspaper]] = await session.execute(
        select(Newspaper).order_by(Newspaper.id)
    )
    return list(result.scalars().all())
