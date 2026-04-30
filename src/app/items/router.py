from fastapi import APIRouter, Depends, HTTPException, status
from app.items.schemas import (
    BookCreate,
    BookResponse,
    MagazineCreate,
    MagazineResponse,
)
from app.items.services import create_book, get_book, get_book_by_id, create_magazine, get_magazine, get_magazine_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import session_maker
from typing import Optional

item_router = APIRouter(tags=["Items"], prefix="/item")




# book views
book_router = APIRouter(tags=["Book"], prefix="/book")

@book_router.post("create_book/", response_model=BookResponse)
async def create_book_view(
    book: BookCreate, session: AsyncSession = Depends(session_maker)
) -> BookResponse:
    return await create_book(session=session, book_data=book)
    


@book_router.get("get_book/", response_model=list[BookResponse])
async def get_book_view(session: AsyncSession = Depends(session_maker)) -> list[BookResponse]:
    return await get_book(session=session)


@book_router.get("get_book_by_id/{book_id}", response_model=Optional[BookResponse])
async def get_book_by_id_view(
    book_id: int, session: AsyncSession = Depends(session_maker)
) -> Optional[BookResponse]:
    book = await get_book_by_id(session=session, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return None

    return BookResponse.model_validate(book)




#magazine_views
magazine_router = APIRouter(tags=["Magazines"], prefix="/magazine")

magazine_router.post("create_magazine/", response_model=MagazineResponse)
async def create_magazine_view(magazine_data: MagazineCreate, session:AsyncSession = Depends(session_maker)) -> MagazineResponse:
    return await create_magazine(session=session, magazine_data=magazine_data)

magazine_router.get("get_magazine/", response_model=list[MagazineResponse])
async def get_magazine_view(session: AsyncSession = Depends(session_maker)) -> list[MagazineResponse]:
    return await get_magazine(session=session)

magazine_router.get("get_book_by_id/{magazine_id}/", response_model=MagazineResponse)
async def get_magazine_by_id_view(magazine_id: int, session: AsyncSession = Depends(session_maker)) -> Optional[MagazineResponse]:
    magazine = await get_magazine_by_id(session=session, magazine_id=magazine_id)
    if magazine is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return f"The magazine with id: {id} is not found"
    return MagazineResponse.model_validate(magazine)