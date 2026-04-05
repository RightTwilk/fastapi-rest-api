from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from typing import Optional
from sqlalchemy import Numeric, Enum
from models.items_models_package.lang_enum import Language
from decimal import Decimal


class Item(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[str]
    publisher: Mapped[str] = mapped_column(nullable=False)
    language: Mapped[Language] = mapped_column(Enum(Language), nullable=False)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2), nullable=False)
