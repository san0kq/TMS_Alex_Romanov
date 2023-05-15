from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import TransactionDTO


class TransactionDAO(BaseDAO):
    def create(self, data: TransactionDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO transactions('
                                        'basket_id,'
                                        'card_id,'
                                        'price,'
                                        'adress_id)'
                                        'VALUES (?, ?, ?, ?);',
                                        (data.basket_id,
                                         data.card_id,
                                         data.price, data.adress_id))
        self._db_gateway.connection.commit()
