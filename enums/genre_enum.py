from enum import Enum


class BookGenre(str, Enum):
    FICTION = "fiction"  # Художественная литература
    SCIENCE_FICTION = "science_fiction"  # Научная фантастика
    FANTASY = "fantasy"  # Фэнтези
    DETECTIVE = "detective"  # Детектив
    THRILLER = "thriller"  # Триллер
    ROMANCE = "romance"  # Романтика
    HISTORICAL = "historical"  # Исторический роман
    ADVENTURE = "adventure"  # Приключения
    HORROR = "horror"  # Ужасы
    BIOGRAPHY = "biography"  # Биография
    SCIENCE = "science"  # Научно-популярная литература
    POETRY = "poetry"  # Поэзия
    DRAMA = "drama"  # Драма
    COMEDY = "comedy"  # Комедия
    CHILDREN = "children"  # Детская литература
