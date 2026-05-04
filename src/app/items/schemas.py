from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from app.items.enums import (
    Month,
    Season,
    Periodicity,
    Theme,
    CoverType,
    Language,
    BookGenre,
)


class ItemBase(BaseModel):
    title: str = Field(..., min_length=1)
    publication_year: int = Field(..., ge=1450, le=2026)
    publisher: str = Field(..., min_length=1)
    language: Language
    price: Decimal = Field(..., ge=0, max_digits=10, decimal_places=2)


class BookBase(ItemBase):
    author: str = Field(..., min_length=1)
    isbn: Optional[str] = Field(None, pattern=r"^\d{13}$")
    page_count: Optional[int] = Field(None, ge=1)
    genre: Optional[BookGenre] = None
    cover_type: Optional[CoverType] = None


class MagazineBase(ItemBase):
    issue_number: int = Field(..., ge=1)
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    month: Optional[Month] = None
    season: Optional[Season] = None
    periodicity: Optional[Periodicity] = None
    theme: Optional[Theme] = None


class NewspaperBase(ItemBase):
    issue_date: date
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    city: Optional[str] = None
    chief_editor: Optional[str] = None
    pages: Optional[int] = Field(None, ge=1)


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class MagazineResponse(MagazineBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class NewspaperResponse(NewspaperBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class MagazineCreate(MagazineBase):
    pass


class NewspaperCreate(NewspaperBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    publication_year: Optional[int] = Field(None, ge=1450, le=2026)
    publisher: Optional[str] = Field(None, min_length=1)
    language: Optional[Language] = None
    price: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    author: Optional[str] = Field(None, min_length=1)
    isbn: Optional[str] = Field(None, pattern=r"^\d{13}$")
    page_count: Optional[int] = Field(None, ge=1)
    genre: Optional[BookGenre] = None
    cover_type: Optional[CoverType] = None


class MagazineUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    publication_year: Optional[int] = Field(None, ge=1450, le=2026)
    publisher: Optional[str] = Field(None, min_length=1)
    language: Optional[Language] = None
    price: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    issue_number: Optional[int] = Field(None, ge=1)
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    month: Optional[Month] = None
    season: Optional[Season] = None
    periodicity: Optional[Periodicity] = None
    theme: Optional[Theme] = None


class NewspaperUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    publication_year: Optional[int] = Field(None, ge=1450, le=2026)
    publisher: Optional[str] = Field(None, min_length=1)
    language: Optional[Language] = None
    price: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    issue_date: Optional[date] = None
    issn: Optional[str] = Field(None, pattern=r"^\d{4}-\d{4}$")
    city: Optional[str] = None
    chief_editor: Optional[str] = None
    pages: Optional[int] = Field(None, ge=1)
