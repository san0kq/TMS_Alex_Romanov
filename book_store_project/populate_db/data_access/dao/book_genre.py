from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BookGenreDTO


class BookGenreDAO(BaseDAO):
    def create(self, data: BookGenreDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO books_genres('
                                        'book_id,'
                                        'genre_id)'
                                        'VALUES (?, ?);',
                                        (data.book_id, data.genre_id))
        self._db_gateway.connection.commit()
