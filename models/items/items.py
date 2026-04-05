from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from typing import Optional
from sqlalchemy import Date

class Item(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str]
    publication_year: Mapped[Date]
    publisher: Mapped[str]
    language: Mapped[str]