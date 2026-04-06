from pydantic import Field
from typing import Optional
from enums.month_enum import Month
from enums.periodicy_enum import Periodicity
from enums.season_enum import Season
from enums.theme_enum import Theme
from schemas.items_schemas_package.item_schema import ItemSchema





class MagazineSchema(ItemSchema):
    issue_number: int = Field(ge=1)
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    month: Optional[Month] = Field(None, ge=1, le=12)
    season: Optional[Season] = None
    periodicity: Optional[Periodicity] = None
    theme: Optional[Theme] = None
