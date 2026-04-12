from sqlalchemy import CheckConstraint, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from sqlalchemy import Enum
from enums.cover_enum import CoverType
from models.items_models_package.items_models import ItemModel  # ваш абстрактный класс


class Book(ItemModel):

    author: Mapped[str] = mapped_column(String(255), nullable=False)
    isbn: Mapped[Optional[str]] = mapped_column(String(13), unique=True)
    page_count: Mapped[Optional[int]] = mapped_column(Integer)
    genre: Mapped[Optional[str]] = mapped_column(String(100))
    cover_type: Mapped[Optional[CoverType]] = mapped_column(Enum(CoverType))

    __table_args__ = (
        CheckConstraint("page_count > 0", name="ck_book_page_count_positive"),
    )
