from providers import gateway_provider
from data_access.dao import UserDAO, BookDAO, AuthorDAO, TransactionDAO


class UsersData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = UserDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str()
        for user in self._dao.list():
            result += (f'ID: {user[0]}\nFirst name: {user[1]}\n'
                       f'Last name: {user[2]}\nEmail: {user[3]}\n'
                       f'Created at: {user[4]}\n\n')
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
        if column == 'email':
            self._dao.email_exist(email=value)
        self._dao.update(user_id=user_id, column=column, value=value)
        return f'The user with ID {user_id} has been successfully updated.'


class BookData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = BookDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str()
        for book in self._dao.list():
            result += (f'ID: {book[0]}\nName: {book[1]}\n'
                       f'Pages: {book[2]}\nPrice: {book[3]}\n'
                       f'Age limit: {book[4]}\nCount: {book[5]}\n\n')
        return result

    def book_info(self, book_id: int) -> str:
        book_info = self._dao.book_info(book_id=book_id)
        book = book_info[0][0]
        authors = [author[0] + ' ' + author[1] for author in book_info[1]]
        genres = [genre[0] for genre in book_info[2]]
        result = (f'ID: {book[0]}\nName: {book[1]}\nAge limit: {book[2]}'
                  f'\nPrice: {book[3]}\nDescription: {book[4]}\n'
                  f'Authors: {authors}\nPages: {book[5]}\nGenres: {genres}\n'
                  f'Format: {book[6]}\nCount: {book[7]}\n'
                  f'Added to shop: {book[8]}\n')

        return result

    def delete(self, book_id: int) -> str:
        self._dao.delete(book_id=book_id)
        return f'The book with ID {book_id} has been successfully deleted.'

    def update(self, book_id: int, value: str) -> str:
        self._dao.update(book_id=book_id, value=value)
        return f'The book with ID {book_id} has been successfully updated.'


class AuthorData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = AuthorDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str()
        for author in self._dao.list():
            result += (f'ID: {author[0]}\nFirst name: {author[1]}\n'
                       f'Last name: {author[2]}\n\n')
        return result

    def author_info(self, author_id: int) -> str:
        author_info = self._dao.author_info(author_id=author_id)
        author = author_info[0]
        result = (f'ID: {author[0]}\nFirst name: {author[1]}\n'
                  f'Last name: {author[2]}\nBirth date: {author[3]}\n'
                  f'Death date: {author[4]}\nInformation: {author[5]}\n')

        return result


class TransactionData:
    def __init__(self) -> None:
        self._db_gateway = gateway_provider()
        self._dao = TransactionDAO(db_gateway=self._db_gateway)

    def list(self) -> str:
        result = str()
        for transaction in self._dao.list():
            result += (f'First name: {transaction[0]}\n'
                       f'Last name: {transaction[1]}\n'
                       f'Card number: {transaction[2]}\n'
                       f'Total price: {transaction[3]}\n'
                       f'Created at: {transaction[4]}\n'
                       f'Adress: {transaction[5]}, {transaction[6]}, '
                       f'{transaction[7]}, {transaction[8]}, postcode: '
                       f'{transaction[9]}\n\n')
        return result
