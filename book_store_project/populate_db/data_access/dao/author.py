from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import AuthorDTO


class AuthorDAO(BaseDAO):
    def create(self, data: AuthorDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO authors('
                                        'first_name,'
                                        'last_name,'
                                        'birth_date,'
                                        'death_date,'
                                        'information)'
                                        'VALUES (?, ?, ?, ?, ?);',
                                        (data.first_name, data.last_name,
                                         data.birth_date, data.death_date,
                                         data.information))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM authors;')
        return result.fetchall()
