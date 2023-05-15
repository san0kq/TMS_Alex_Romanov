from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import GenreDTO


class GenreDAO(BaseDAO):
    def create(self, data: GenreDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO genres('
                                        'name,'
                                        'description)'
                                        'VALUES (?, ?);',
                                        (data.name, data.description))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM genres;')
        return result.fetchall()
