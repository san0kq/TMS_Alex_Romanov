from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BookBasketDTO


class BookBasketDAO(BaseDAO):
    def create(self, data: BookBasketDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO books_baskets('
                                        'book_id,'
                                        'basket_id)'
                                        'VALUES (?, ?);',
                                        (data.book_id, data.basket_id))
        self._db_gateway.connection.commit()
