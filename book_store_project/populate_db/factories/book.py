from __future__ import annotations
from typing import TYPE_CHECKING
from random import randint, uniform

if TYPE_CHECKING:
    from rand_gen import RandGen
from data_access.dto import BookDTO


class BookFactory:
    def __init__(
            self,
            name_provider: RandGen,
            description: RandGen,
    ) -> None:
        self._name_provider = name_provider
        self._description = description

    def generate(self) -> BookDTO:
        return BookDTO(
            name=self._name_provider.generate(randint(5, 15)),
            price=round(uniform(1, 10000), 2),
            description=self._description.generate(randint(10, 20)),
            pages=randint(50, 1000)
        )
