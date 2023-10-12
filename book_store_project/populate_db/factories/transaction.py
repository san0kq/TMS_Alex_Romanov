from __future__ import annotations
from random import uniform
from typing import TYPE_CHECKING

from data_access.dto import TransactionDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class TransactionFactory:
    def __init__(
            self,
            basket_id_provider: RandomValueFromListProvider,
            card_id_provider: RandomValueFromListProvider,
            adress_id_provider: RandomValueFromListProvider
    ) -> None:
        self._basket_id_provider = basket_id_provider
        self._card_id_provider = card_id_provider
        self._adress_id_provider = adress_id_provider

    def generate(self) -> TransactionDTO:
        return TransactionDTO(
            basket_id=self._basket_id_provider(),
            card_id=self._card_id_provider(),
            price=round(uniform(1, 10000), 2),
            adress_id=self._adress_id_provider()
        )
