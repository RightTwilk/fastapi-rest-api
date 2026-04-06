from sqlalchemy.orm import Mapped, mapped_column
from models.items_models_package.items_models import ItemModel
from sqlalchemy import CheckConstraint, String, Integer, Date
from datetime import date
from typing import Optional


class Newspaper(ItemModel):
    issue_date: Mapped[date] = mapped_column(Date, nullable=False)
    issn: Mapped[Optional[str]] = mapped_column(String(9))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    chief_editor: Mapped[Optional[str]] = mapped_column(String(255))
    pages: Mapped[Optional[int]] = mapped_column(Integer)

    __table_args__ = (CheckConstraint("pages > 0", name="ck_newspaper_pages_positive"),)
