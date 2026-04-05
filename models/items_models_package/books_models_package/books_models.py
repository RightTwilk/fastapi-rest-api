from sqlalchemy.orm import Mapped, mapped_column
from models.items_models_package.items_models import Item
from models.items_models_package.books_models_package.genre_enum import BookGenre
from models.items_models_package.books_models_package.cover_enum import CoverType

from sqlalchemy import Enum


class Book(Item):
    author: Mapped[str] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(nullable=False)
    page_count: Mapped[int]
    genre: Mapped[BookGenre] = mapped_column(Enum(BookGenre))
    cover_type: Mapped[CoverType] = mapped_column(Enum(CoverType))
