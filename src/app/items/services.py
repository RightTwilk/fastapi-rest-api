from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from app.items.models import Book
from app.items.schemas import BookCreate


# books
async def get_book(session: AsyncSession) -> list[Book]:
    result: Result[tuple[Book]] = await session.execute(select(Book).order_by(Book.id))
    return list(result.scalars().all())


async def get_book_by_id(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def create_book(session: AsyncSession, book_data: BookCreate) -> Book:
    book_model = Book(**book_data.model_dump())
    session.add(book_model)
    await session.commit()
    await session.refresh(book_model)
    return book_model
