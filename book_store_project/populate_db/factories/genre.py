from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING

from data_access.dto import GenreDTO
if TYPE_CHECKING:
    from rand_gen import RandGen


class GenreFactory:
    def __init__(
            self,
            name_provider: RandGen,
            description_provider: RandGen
    ) -> None:
        self._name_provider = name_provider
        self._description_provider = description_provider

    def generate(self) -> GenreDTO:
        return GenreDTO(
            name=self._name_provider.generate(randint(3, 7)),
            description=self._description_provider.generate(randint(5, 10))
        )
