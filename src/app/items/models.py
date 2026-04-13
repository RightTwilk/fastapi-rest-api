from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import Date, Numeric, Enum, CheckConstraint, Sequence, String, Integer
from typing import Optional
from app.items.enums import Month, Season, Periodicity, Theme, CoverType, Language, BookGenre
from decimal import Decimal
from app.models.base import Base

global_items_id = Sequence("global_id", start=1, increment=1, metadata=Base.metadata)


class ItemModel(Base):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True, server_default=global_items_id.next_value()
    )
    title: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[int]
    publisher: Mapped[str] = mapped_column(nullable=False)
    language: Mapped[Language] = mapped_column(Enum(Language), nullable=False)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "publication_year BETWEEN 1450 AND 2026", name="check_year_range"
        ),
        CheckConstraint("price >= 0", name="check_price_non_negative"),
        CheckConstraint("title <> ''", name="check_title_not_empty"),
    )

class Book(ItemModel):

    author: Mapped[str] = mapped_column(String(255), nullable=False)
    isbn: Mapped[Optional[str]] = mapped_column(String(13), unique=True)
    page_count: Mapped[Optional[int]] = mapped_column(Integer)
    genre: Mapped[BookGenre] = mapped_column(Enum(BookGenre))
    cover_type: Mapped[Optional[CoverType]] = mapped_column(Enum(CoverType))

    __table_args__ = (
        CheckConstraint("page_count > 0", name="ck_book_page_count_positive"),
    )

class Magazine(ItemModel):
    issue_number: Mapped[int] = mapped_column(Integer, nullable=False)
    issn: Mapped[Optional[str]] = mapped_column(String(9), unique=True)
    month: Mapped[Optional[Month]] = mapped_column(Enum(Month))
    season: Mapped[Optional[Season]] = mapped_column(Enum(Season))
    periodicity: Mapped[Optional[Periodicity]] = mapped_column(Enum(Periodicity))
    theme: Mapped[Optional[Theme]] = mapped_column(Enum(Theme))

    __table_args__ = (
        CheckConstraint("issue_number > 0", name="ck_magazine_issue_number_positive"),
    )

class Newspaper(ItemModel):
    issue_date: Mapped[date] = mapped_column(Date, nullable=False)
    issn: Mapped[Optional[str]] = mapped_column(String(9))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    chief_editor: Mapped[Optional[str]] = mapped_column(String(255))
    pages: Mapped[Optional[int]] = mapped_column(Integer)

    __table_args__ = (CheckConstraint("pages > 0", name="ck_newspaper_pages_positive"),)
