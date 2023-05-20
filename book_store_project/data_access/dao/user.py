from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
from ..errors import RecordExistsError
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

    def list(self) -> list[str]:
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'users.id, '
                                                 'first_name, '
                                                 'last_name, '
                                                 'email, '
                                                 'registered_at FROM '
                                                 'users JOIN profiles ON '
                                                 'profile_id = profiles.id '
                                                 'ORDER BY first_name, '
                                                 'last_name;')

        return result.fetchall()

    def user_info(self, user_id: int) -> tuple[list[str], list[str]]:
        if user_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'User with ID {user_id} does not exist.')
        user_result = self._db_gateway.cursor.execute('SELECT '
                                                      'users.id, '
                                                      'first_name, '
                                                      'last_name, '
                                                      'email, '
                                                      'phone, '
                                                      'age, '
                                                      'registered_at FROM '
                                                      'users JOIN profiles ON '
                                                      'profile_id = '
                                                      'profiles.id '
                                                      'WHERE users.id = ?;',
                                                      (user_id, ))
        user_result = user_result.fetchall()

        roles_result = self._db_gateway.cursor.execute('SELECT roles.name '
                                                       'FROM users_roles JOIN '
                                                       'users ON user_id = '
                                                       'users.id  '
                                                       'JOIN roles ON '
                                                       'role_id = '
                                                       'roles.id '
                                                       'WHERE users.id = ?;',
                                                       (user_id, ))
        roles_result = roles_result.fetchall()

        return user_result, roles_result

    def delete(self, user_id: int) -> None:
        if user_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'User with ID {user_id} does not exist.')
        self._db_gateway.cursor.execute('DELETE FROM users WHERE id = ?;',
                                        (user_id, ))
        self._db_gateway.connection.commit()

    def update(self, user_id: int, column: str, value: str) -> None:
        if user_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'User with ID {user_id} does not exist.')
        self._db_gateway.cursor.execute(
            f'UPDATE profiles SET {column} = ? WHERE id = ?',
            (value, user_id)
        )
        self._db_gateway.connection.commit()

    def email_exist(self, email: str) -> None:
        self._db_gateway.cursor.execute('SELECT * FROM profiles WHERE '
                                        'email = ?', (email, ))
        if self._db_gateway.cursor.fetchall():
            raise RecordExistsError(f'The email address {email} '
                                    f'already exists.')
