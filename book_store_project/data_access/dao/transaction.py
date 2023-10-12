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

    def list(self) -> list[str]:
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'profiles.first_name, '
                                                 'profiles.last_name, '
                                                 'number, '
                                                 'price, '
                                                 'transactions.created_at, '
                                                 'country, '
                                                 'city, '
                                                 'street, '
                                                 'house_number, '
                                                 'postcode '
                                                 'FROM transactions JOIN '
                                                 'baskets ON basket_id = '
                                                 'baskets.id JOIN users ON '
                                                 'baskets.user_id = users.id '
                                                 'JOIN profiles ON '
                                                 'users.profile_id = '
                                                 'profiles.id JOIN bankcards '
                                                 'ON card_id = bankcards.id '
                                                 'JOIN adresses ON '
                                                 'adress_id = adresses.id;'
                                                 )

        return result.fetchall()
