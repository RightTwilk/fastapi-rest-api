from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from decimal import Decimal

from app.items.enums import Month, Season, Periodicity, Theme, CoverType, Language, BookGenre



class ItemSchema(BaseModel):
    id: int = Field(ge=1)
    title: str = Field(min_length=1)
    publication_year: int = Field(ge=1450, le=2026)
    publisher: str = Field(min_length=1)
    language: Language
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)

class BookSchema(ItemSchema):
    author: str = Field(min_length=1)
    isbn: Optional[str] = Field(None, pattern=r"^\d{13}$")
    page_count: Optional[int] = Field(None, ge=1)
    genre: Optional[BookGenre] = None
    cover_type: Optional[CoverType] = None

class MagazineSchema(ItemSchema):
    issue_number: int = Field(ge=1)
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    month: Optional[Month] = Field(None, ge=1, le=12)
    season: Optional[Season] = None
    periodicity: Optional[Periodicity] = None
    theme: Optional[Theme] = None

class NewspaperSchema(ItemSchema):
    issue_date: date
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    city: Optional[str] = None
    chief_editor: Optional[str] = None
    pages: Optional[int] = Field(None, ge=1)
