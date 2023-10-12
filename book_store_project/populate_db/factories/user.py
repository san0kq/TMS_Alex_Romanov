from __future__ import annotations

from random import choice, randint
import datetime
from time import time
from typing import TYPE_CHECKING

from data_access.dto import UserDTO, ProfileDTO, BasketDTO, BankCardDTO
if TYPE_CHECKING:
    from ..rand_gen import RandGen


class UserFactory:
    def __init__(
            self,
            username_provider: RandGen,
            password_provider: RandGen,
            first_name_provider: RandGen,
            last_name_provider: RandGen,
            email_provider: RandGen,
            phone_provider: RandGen,
            number_provider: RandGen,

    ) -> None:
        self._username_provider = username_provider
        self._password_provider = password_provider
        self._first_name_provider = first_name_provider
        self._last_name_provider = last_name_provider
        self._email_provider = email_provider
        self._phone_provider = phone_provider
        self._number_provider = number_provider

    def generate(self) -> UserDTO:

        profile = ProfileDTO(
            first_name=self._first_name_provider.generate(randint(4, 10)),
            last_name=self._last_name_provider.generate(randint(4, 10)),
            age=randint(18, 99),
            email=self._email_provider.generate(randint(5, 10)),
            phone=self._phone_provider.generate()
        )
        basket = BasketDTO(status=choice(('Paid', 'Active')))
        bank_card = BankCardDTO(
            number=self._number_provider.generate(),
            first_name=self._first_name_provider.generate(randint(4, 10)),
            last_name=self._last_name_provider.generate(randint(4, 10)),
            cvc=randint(100, 999),
            period=datetime.datetime.fromtimestamp(
                randint(int(time()),
                        int(time() + 315532800))).strftime('%Y-%m')
        )
        return UserDTO(
            username=self._username_provider.generate(randint(4, 10)),
            password=self._password_provider.generate(randint(8, 20)),
            profile=profile,
            basket=basket,
            bank_card=bank_card
        )
