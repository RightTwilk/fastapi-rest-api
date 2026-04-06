from pydantic import BaseModel, Field
from decimal import Decimal
from enums.lang_enum import Language


class ItemSchema(BaseModel):
    id: int = Field(ge=1)
    title: str = Field(min_length=1)
    publication_year: int = Field(ge=1450, le=2026)
    publisher: str = Field(min_length=1)
    language: Language
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
