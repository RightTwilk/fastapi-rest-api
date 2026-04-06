from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from typing import Optional
from sqlalchemy import Numeric, Enum, CheckConstraint
from enums.lang_enum import Language
from decimal import Decimal


class ItemModel(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[int]
    publisher: Mapped[str] = mapped_column(nullable=False)
    language: Mapped[Language] = mapped_column(Enum(Language), nullable=False)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("publication_year BETWEEN 1450 AND 2026", name="check_year_range"),
        CheckConstraint("price >= 0", name="check_price_non_negative"),
        CheckConstraint("title <> ''", name="check_title_not_empty"),
    )