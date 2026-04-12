from models.items_models_package.items_models import ItemModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint, Integer, String, Enum
from typing import Optional
from enums.month_enum import Month
from enums.periodicy_enum import Periodicity
from enums.season_enum import Season
from enums.theme_enum import Theme


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
