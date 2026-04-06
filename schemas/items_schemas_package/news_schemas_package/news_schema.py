from pydantic import Field
from schemas.items_schemas_package.item_schema import ItemSchema
from datetime import date
from typing import Optional


class NewspaperSchema(ItemSchema):
    issue_date: date
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    city: Optional[str] = None
    chief_editor: Optional[str] = None
    pages: Optional[int] = Field(None, ge=1)