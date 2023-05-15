from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BookDTO


class BookDAO(BaseDAO):
    def create(self, data: BookDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO books ('
                                        'name,'
                                        'price,'
                                        'description,'
                                        'pages) VALUES'
                                        '(?, ?, ?, ?);',
                                        (data.name, data.price,
                                         data.description, data.pages))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM books;')
        return result.fetchall()
    
    def list(self) -> list[str]:
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'book.id, '
                                                 'first_name, '
                                                 'last_name, '
                                                 'email, '
                                                 'registered_at FROM '
                                                 'users JOIN profiles ON '
                                                 'profile_id = profiles.id '
                                                 'ORDER BY first_name, '
                                                 'last_name;')

        return result.fetchall()