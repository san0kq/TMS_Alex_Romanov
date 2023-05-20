from dataclasses import dataclass


@dataclass
class BookDTO:
    name: str
    price: float
    description: str
    pages: int
    format_id: int
    age_limit: int
    count: int
