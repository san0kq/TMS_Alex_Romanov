from __future__ import annotations
from typing import TYPE_CHECKING

from data_access.dto import RolePermissionDTO
if TYPE_CHECKING:
    from providers import RandomValueFromListProvider


class RolePermissionFactory:
    def __init__(
            self,
            role_id_provider: RandomValueFromListProvider,
            permission_id_provider: RandomValueFromListProvider
    ) -> None:
        self._role_id_provider = role_id_provider
        self._permission_id_provider = permission_id_provider

    def generate(self) -> RolePermissionDTO:
        return RolePermissionDTO(
            role_id=self._role_id_provider(),
            permission_id=self._permission_id_provider()
        )
