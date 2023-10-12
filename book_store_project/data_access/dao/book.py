from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
from ..errors import RecordExistsError
if TYPE_CHECKING:
    from dto import BookDTO


class BookDAO(BaseDAO):
    def create(self, data: BookDTO) -> None:
        self._db_gateway.cursor.execute('INSERT INTO books ('
                                        'name,'
                                        'price,'
                                        'description,'
                                        'pages,'
                                        'format_id,'
                                        'age_limit,'
                                        'count) VALUES'
                                        '(?, ?, ?, ?, ?, ?, ?);',
                                        (data.name, data.price,
                                         data.description, data.pages,
                                         data.format_id, data.age_limit,
                                         data.count))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute('SELECT id FROM books;')
        return result.fetchall()

    def list(self) -> list[str]:
        result = self._db_gateway.cursor.execute('SELECT '
                                                 'id, '
                                                 'name, '
                                                 'pages, '
                                                 'price, '
                                                 'age_limit, '
                                                 'count FROM '
                                                 'books '
                                                 'ORDER BY name;'
                                                 )

        return result.fetchall()

    def book_info(self, book_id: int) -> tuple[list[str],
                                               list[str],
                                               list[str]]:
        if book_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'Book with ID {book_id} does not exist.')
        book_result = self._db_gateway.cursor.execute('SELECT '
                                                      'books.id, '
                                                      'books.name, '
                                                      'age_limit, '
                                                      'price, '
                                                      'description, '
                                                      'pages, '
                                                      'formats.name, '
                                                      'count, '
                                                      'created_at FROM '
                                                      'books JOIN formats ON '
                                                      'format_id = '
                                                      'formats.id '
                                                      'WHERE books.id = ?;',
                                                      (book_id, ))
        book_result = book_result.fetchall()

        authors_result = self._db_gateway.cursor.execute('SELECT first_name, '
                                                         'last_name ' 
                                                         'FROM books_authors '
                                                         'JOIN books ON '
                                                         'book_id = books.id '
                                                         'JOIN authors ON '
                                                         'author_id = '
                                                         'authors.id '
                                                         'WHERE books.id = ?;',
                                                         (book_id, ))
        authors_result = authors_result.fetchall()

        genres_result = self._db_gateway.cursor.execute('SELECT genres.name '
                                                        'FROM '
                                                        'books_genres JOIN '
                                                        'books ON book_id = '
                                                        'books.id JOIN genres '
                                                        'ON genre_id = '
                                                        'genres.id WHERE '
                                                        'books.id = ?;',
                                                        (book_id, ))
        genres_result = genres_result.fetchall()

        return book_result, authors_result, genres_result

    def delete(self, book_id: int) -> None:
        if book_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'Book with ID {book_id} does not exist.')
        self._db_gateway.cursor.execute('DELETE FROM books WHERE id = ?;',
                                        (book_id, ))
        self._db_gateway.connection.commit()

    def update(self, book_id: int, value: str) -> None:
        if book_id not in [id[0] for id in self.get_ids_list()]:
            raise RecordExistsError(f'Book with ID {book_id} does not exist.')
        self._db_gateway.cursor.execute(
            'UPDATE books SET name = ? WHERE id = ?',
            (value, book_id)
        )
        self._db_gateway.connection.commit()
