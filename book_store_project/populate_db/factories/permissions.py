from __future__ import annotations
from typing import TYPE_CHECKING
from random import randint

if TYPE_CHECKING:
    from rand_gen import RandGen
from data_access.dto import PermissionDTO


class PermissionFactory:
    def __init__(
            self,
            name_provider: RandGen
    ) -> None:
        self._name_provider = name_provider

    def generate(self) -> PermissionDTO:
        return PermissionDTO(name=self._name_provider.generate(randint(5, 10)))
