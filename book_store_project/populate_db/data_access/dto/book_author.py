from dataclasses import dataclass


@dataclass
class BookAuthorDTO:
    book_id: int
    author_id: int
