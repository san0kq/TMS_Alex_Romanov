from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING
import datetime

from data_access.dto import AuthorDTO
if TYPE_CHECKING:
    from rand_gen import RandGen


class AuthorFactory:
    def __init__(
            self,
            first_name_provider: RandGen,
            last_name_provider: RandGen,
            information_provider: RandGen
    ) -> None:
        self._first_name_provider = first_name_provider
        self._last_name_provider = last_name_provider
        self._information_provider = information_provider

    def generate(self) -> AuthorDTO:
        return AuthorDTO(
            first_name=self._first_name_provider.generate(randint(4, 10)),
            last_name=self._last_name_provider.generate(randint(4, 10)),
            birth_date=datetime.date(1900, 1, 1)
            + datetime.timedelta(days=randint(0, 36524)),
            death_date=datetime.date(2000, 1, 1)
            + datetime.timedelta(days=randint(0, 8401)),
            information=self._information_provider.generate(randint(10, 20))
        )
