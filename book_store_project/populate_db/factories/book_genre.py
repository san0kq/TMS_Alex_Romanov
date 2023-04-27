from __future__ import annotations
from typing import TYPE_CHECKING

from data_access.dto import BookGenreDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class BookGenreFactory:
    def __init__(
            self,
            book_id_provider: RandomValueFromListProvider,
            genre_id_provider: RandomValueFromListProvider
    ) -> None:
        self._book_id_provider = book_id_provider
        self._genre_id_provider = genre_id_provider

    def generate(self) -> BookGenreDTO:
        return BookGenreDTO(
            book_id=self._book_id_provider(),
            genre_id=self._genre_id_provider()
        )
