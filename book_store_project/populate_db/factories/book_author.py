from __future__ import annotations
from typing import TYPE_CHECKING

from data_access.dto import BookAuthorDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class BookAuthorFactory:
    def __init__(
            self,
            book_id_provider: RandomValueFromListProvider,
            author_id_provider: RandomValueFromListProvider
    ) -> None:
        self._book_id_provider = book_id_provider
        self._author_id_provider = author_id_provider

    def generate(self) -> BookAuthorDTO:
        return BookAuthorDTO(
            book_id=self._book_id_provider(),
            author_id=self._author_id_provider()
        )
