from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING

from data_access.dto import FormatDTO
if TYPE_CHECKING:
    from rand_gen import RandGen


class FormatFactory:
    def __init__(
            self,
            name_provider: RandGen,
    ) -> None:
        self._name_provider = name_provider

    def generate(self) -> FormatDTO:
        return FormatDTO(
            name=self._name_provider.generate(randint(5, 10))
        )
