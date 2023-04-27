from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING

from data_access.dto import AdressDTO
if TYPE_CHECKING:
    from rand_gen import RandGen
    from providers import RandomValueFromListProvider


class AdressFactory:
    def __init__(
            self,
            country_provider: RandGen,
            city_provider: RandGen,
            street_provider: RandGen,
            user_id_provider: RandomValueFromListProvider
    ) -> None:
        self._country_provider = country_provider
        self._city_provider = city_provider
        self._street_provider = street_provider
        self._user_id_provider = user_id_provider

    def generate(self) -> AdressDTO:
        return AdressDTO(
            country=self._country_provider.generate(randint(5, 10)),
            city=self._city_provider.generate(randint(5, 10)),
            street=self._street_provider.generate(randint(5, 10)),
            house_number=randint(1, 50),
            postcode=randint(11111, 99999),
            user_id=self._user_id_provider()
        )
