from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import FormatDTO


class FormatDAO(BaseDAO):
    def create(self, data: FormatDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO formats('
                                        'name) '
                                        'VALUES (?);',
                                        (data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM formats;')
        return result.fetchall()
