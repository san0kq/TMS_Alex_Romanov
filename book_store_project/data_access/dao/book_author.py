from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BookAuthorDTO


class BookAuthorDAO(BaseDAO):
    def create(self, data: BookAuthorDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO books_authors('
                                        'book_id,'
                                        'author_id)'
                                        'VALUES (?, ?);',
                                        (data.book_id, data.author_id))
        self._db_gateway.connection.commit()
