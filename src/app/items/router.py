from fastapi import APIRouter, Depends
from app.items.schemas import BookCreate
from app.items.services import create_book
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import session_maker


item_router = APIRouter(tags=["Items"], prefix="/items")


@item_router.post("create_book/", response_model=None)
async def create_book_view(
    book: BookCreate, session: AsyncSession = Depends(session_maker)
):
    await create_book(session=session, book_data=book)
    return {'BookCreate':'Succes'}