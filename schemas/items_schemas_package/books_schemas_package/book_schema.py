from schemas.items_schemas_package.item_schema import ItemSchema
from typing import Optional
from pydantic import Field
from enums.cover_enum import CoverType
from enums.genre_enum import BookGenre


class BookSchema(ItemSchema):
    author: str = Field(min_length=1)
    isbn: Optional[str] = Field(None, pattern=r"^\d{13}$")
    page_count: Optional[int] = Field(None, ge=1)
    genre: Optional[BookGenre] = None
    cover_type: Optional[CoverType] = None
