from dataclasses import dataclass


@dataclass
class BookDTO:
    name: str
    price: float
    description: str
    pages: int
