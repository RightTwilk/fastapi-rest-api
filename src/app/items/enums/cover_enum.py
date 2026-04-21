from enum import Enum


class CoverType(str, Enum):
    HARDCOVER = "hardcover"  
    SOFTCOVER = "softcover"  
    DUST_JACKET = "dust_jacket" 
    LEATHER = "leather"  
    PAPERBACK = "paperback"  
    SPIRAL = "spiral"  
    BOARD_BOOK = "board_book"  
