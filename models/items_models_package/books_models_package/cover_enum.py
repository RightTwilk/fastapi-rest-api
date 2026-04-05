from enum import Enum


class CoverType(str, Enum):
    HARDCOVER = "hardcover"  # Твёрдый переплёт
    SOFTCOVER = "softcover"  # Мягкая обложка
    DUST_JACKET = "dust_jacket"  # Суперобложка
    LEATHER = "leather"  # Кожаный переплёт
    PAPERBACK = "paperback"  # Бумажная обложка (часто синоним softcover)
    SPIRAL = "spiral"  # Спиральный переплёт
    BOARD_BOOK = "board_book"  # Картонная обложка (для детских книг)
