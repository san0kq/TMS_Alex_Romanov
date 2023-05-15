from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import AdressDTO


class AdressDAO(BaseDAO):
    def create(self, data: AdressDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO adresses('
                                        'country,'
                                        'city,'
                                        'street,'
                                        'house_number,'
                                        'postcode,'
                                        'user_id)'
                                        'VALUES (?, ?, ?, ?, ?, ?);',
                                        (data.country, data.city,
                                         data.street, data.house_number,
                                         data.postcode, data.user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM adresses;')
        return result.fetchall()
