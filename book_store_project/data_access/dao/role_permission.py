from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import RolePermissionDTO


class RolePermissionDAO(BaseDAO):
    def create(self, data: RolePermissionDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO roles_permissions('
                                        'role_id,'
                                        'permission_id)'
                                        'VALUES (?, ?);',
                                        (data.role_id, data.permission_id))
        self._db_gateway.connection.commit()
