from providers import gateway_provider
from data_access.dao import UserDAO, BookDAO


class UsersData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = UserDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str() 
        for user in self._dao.list():
            result += (f'ID: {user[0]}\nFirst name: {user[1]}\n'
                       f'Last name: {user[2]}\nEmail: {user[3]}\n'
                       f'Created at: {user[4]}\n')
        return result
    
    def user_info(self, user_id: int) -> str:
        user_info = self._dao.user_info(user_id=user_id)
        user = user_info[0][0]
        roles = [role[0] for role in user_info[1]]
        result = (f'ID: {user[0]}\nFirst name: {user[1]}\nLast name: {user[2]}'
                  f'\nEmail: {user[3]}\nPhone: {user[4]}\nAge: {user[5]}\n'
                  f'Registration date: {user[6]}\nRoles: {roles}')

        return result
    
    def delete(self, user_id: int) -> str:
        self._dao.delete(user_id=user_id)
        return f'The user with ID {user_id} has been successfully deleted.'
    
    def update(self, user_id: int, column: str, value: str) -> str:
        self._dao.update(user_id=user_id, column=column, value=value)
        return f'The user with ID {user_id} has been successfully updated.'



class BookData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = BookDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str() 
        for user in self._dao.list():
            result += (f'ID: {user[0]}\nFirst name: {user[1]}\n'
                       f'Last name: {user[2]}\nEmail: {user[3]}\n'
                       f'Created at: {user[4]}\n')
        return result
    
    def user_info(self, user_id: int) -> str:
        user_info = self._dao.user_info(user_id=user_id)
        user = user_info[0][0]
        roles = [role[0] for role in user_info[1]]
        result = (f'ID: {user[0]}\nFirst name: {user[1]}\nLast name: {user[2]}'
                  f'\nEmail: {user[3]}\nPhone: {user[4]}\nAge: {user[5]}\n'
                  f'Registration date: {user[6]}\nRoles: {roles}')

        return result
    
    def delete(self, user_id: int) -> str:
        self._dao.delete(user_id=user_id)
        return f'The user with ID {user_id} has been successfully deleted.'
    
    def update(self, user_id: int, column: str, value: str) -> str:
        self._dao.update(user_id=user_id, column=column, value=value)
        return f'The user with ID {user_id} has been successfully updated.'