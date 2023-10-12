from __future__ import annotations
from typing import TYPE_CHECKING

from data_access.dto import BookBasketDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class BookBasketFactory:
    def __init__(
            self,
            book_id_provider: RandomValueFromListProvider,
            basket_id_provider: RandomValueFromListProvider
    ) -> None:
        self._book_id_provider = book_id_provider
        self._basket_id_provider = basket_id_provider

    def generate(self) -> BookBasketDTO:
        return BookBasketDTO(
            book_id=self._book_id_provider(),
            basket_id=self._basket_id_provider()
        )
