from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
if TYPE_CHECKING:
    from dto import UserDTO


class UserDAO(BaseDAO):
    def create(self, data: UserDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO profiles ('
                                        'first_name,'
                                        'last_name,'
                                        'age,'
                                        'email,'
                                        'phone)'
                                        'VALUES (?, ?, ?, ?, ?);',
                                        (data.profile.first_name,
                                         data.profile.last_name,
                                         data.profile.age, data.profile.email,
                                         data.profile.phone))
        profile_id = self._db_gateway.cursor.lastrowid
        self._db_gateway.cursor.execute('INSERT INTO users ('
                                        'username,'
                                        'password,'
                                        'profile_id)'
                                        'VALUES (?, ?, ?);',
                                        (data.username, data.password,
                                         profile_id))
        user_id = self._db_gateway.cursor.lastrowid
        self._db_gateway.cursor.execute('INSERT INTO baskets (user_id, status)'
                                        'VALUES (?, ?);',
                                        (user_id, data.basket.status))
        self._db_gateway.cursor.execute('INSERT INTO bankcards ('
                                        'number,'
                                        'first_name,'
                                        'last_name,'
                                        'cvc,'
                                        'period,'
                                        'user_id)'
                                        'VALUES (?, ?, ?, ?, ?, ?);',
                                        (data.bank_card.number,
                                         data.bank_card.first_name,
                                         data.bank_card.last_name,
                                         data.bank_card.cvc,
                                         data.bank_card.period,
                                         user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM users;')
        return result.fetchall()
