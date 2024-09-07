from enum import StrEnum
from rich.color import Color


class Color(StrEnum):
    RED = "red", # Comments
    GREEN = "green", # Strings
    BLUE = "blue", # Functions
    YELLOW = "yellow", # Numbers
    CYAN = "cyan", # Booleans
    ORANGE = "orange", # Keywords
    WHITE = "white" # Operators + Variables
