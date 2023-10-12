from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rand_gen import RandGen

from data_access.dto import RoleDTO


class RoleFactory:
    def __init__(self, name_provider: RandGen) -> None:
        self._name_provider = name_provider

    def generate(self) -> RoleDTO:
        return RoleDTO(name=self._name_provider.generate(randint(4, 10)))
