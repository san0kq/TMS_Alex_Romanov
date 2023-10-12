from __future__ import annotations
from typing import TYPE_CHECKING

from data_access.dto import UserRoleDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class UserRoleFactory:
    def __init__(
            self,
            user_id_provider: RandomValueFromListProvider,
            role_id_provider: RandomValueFromListProvider
    ) -> None:
        self._user_id_provider = user_id_provider
        self._role_id_provider = role_id_provider

    def generate(self) -> UserRoleDTO:
        return UserRoleDTO(
            user_id=self._user_id_provider(),
            role_id=self._role_id_provider()
        )
