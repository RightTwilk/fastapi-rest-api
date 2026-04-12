from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import Numeric, Enum, CheckConstraint, Sequence
from typing import Optional
from enums.lang_enum import Language
from decimal import Decimal
from models.base import Base

global_items_id = Sequence("global_id", start=1, increment=1)


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
