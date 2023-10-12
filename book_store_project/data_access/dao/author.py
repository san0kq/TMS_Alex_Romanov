from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
from ..errors import RecordExistsError
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
                                         data.information
                                         ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM authors;')
        return result.fetchall()

    def list(self) -> list[str]:
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'id, '
                                                 'first_name, '
                                                 'last_name '
                                                 'FROM authors ORDER BY '
                                                 'first_name, last_name;'
                                                 )

        return result.fetchall()

    def author_info(self, author_id: int) -> list[str]:
        if author_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'Author with ID {author_id} does '
                                    f'not exist.')
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'id, '
                                                 'first_name, '
                                                 'last_name, '
                                                 'birth_date, '
                                                 'death_date, '
                                                 'information '
                                                 'FROM '
                                                 'authors WHERE id = ?;',
                                                 (author_id, )
                                                 )
        result = result.fetchall()

        return result
