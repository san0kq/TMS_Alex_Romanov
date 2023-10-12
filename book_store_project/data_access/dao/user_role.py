from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from data_access.dto import UserRoleDTO


class UserRoleDAO(BaseDAO):
    def create(self, data: UserRoleDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO users_roles('
                                        'user_id,'
                                        'role_id)'
                                        'VALUES (?, ?);',
                                        (data.user_id, data.role_id))
        self._db_gateway.connection.commit()
