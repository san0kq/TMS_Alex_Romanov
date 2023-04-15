import sqlite3
from random import randint, uniform
from time import time
import datetime
from typing import Any

from rand_gen import RandGen, RandWord, RandLastName, RandFirstName
from fake_lib import FakeFactory, providers


class DBConnector:
    def __init__(self, db_name: str, count: str) -> None:
        self.db_name = db_name
        self.count = count
        self.connection = sqlite3.connect(f'file:{db_name}?mode=rw', uri=True)
        self.cursor = self.connection.cursor()

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: str) -> None:
        if not value.isdigit():
            raise ValueError('Count must be a positive integer.')
        elif not 0 < int(value) < 1001:
            raise ValueError('Count must be an integer in range (1, 1000).')
        else:
            self._count = int(value)

    @property
    def db_name(self) -> str:
        return self._db_name

    @db_name.setter
    def db_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Database name must be a string')
        elif value.split('.', 1)[1] != 'db':
            raise ValueError('Invalid database name. The file must have '
                             'a .db extension.')
        else:
            self._db_name = value


class DBPopulate(DBConnector):
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        for _ in range(self.count):
            self.profiles()
            self.users()
            self.roles()
            self.permissions()
            self.baskets()
            self.books()
            self.authors()
            self.genres()
            self.bankcards()
            self.adresses()
            self.transactions()
            self.intermediate_tables()
            self.connection.commit()
        self.connection.close()

    def profiles(self) -> None:
        first_name = RandGen(RandFirstName).generate(randint(3, 10))
        last_name = RandGen(RandLastName).generate(randint(3, 15))
        age = randint(18, 99)
        email = FakeFactory(providers.EmailProvider, 1).generate()
        phone = FakeFactory(providers.PhoneProvider, 1).generate()
        try:
            self.cursor.execute('INSERT INTO profiles('
                                'first_name, '
                                'last_name, '
                                'age, '
                                'email, '
                                'phone) '
                                'VALUES (?, ?, ?, ?, ?);',
                                (first_name, last_name, age, email, phone))
            self.profile_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.profiles()

    def users(self) -> None:
        username = RandGen(RandWord).generate(randint(3, 10))
        password = RandGen(RandWord).generate(randint(6, 15))
        try:
            self.cursor.execute('INSERT INTO users('
                                'username,'
                                'password,'
                                'profile_id)'
                                'VALUES (?, ?, ?);', (username, password,
                                                      self.profile_id))
            self.user_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.users()

    def roles(self) -> None:
        name = RandGen(RandWord).generate(randint(5, 10))
        try:
            self.cursor.execute('INSERT INTO roles('
                                'name)'
                                'VALUES (?);', (name,))
            self.role_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.roles()

    def permissions(self) -> None:
        name = RandGen(RandWord).generate(randint(5, 10))
        try:
            self.cursor.execute('INSERT INTO permissions('
                                'name)'
                                'VALUES (?);', (name,))
            self.permission_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.permissions()

    def baskets(self) -> None:
        self.cursor.execute('INSERT INTO baskets('
                            'user_id,'
                            'status)'
                            'VALUES (?, ?);', (self.user_id, 'paid'))
        self.basket_id = self.cursor.lastrowid

    def books(self) -> None:
        name = RandGen(RandWord).generate()
        price = uniform(1, 10000)
        description = RandGen(RandWord).generate(randint(10, 20))
        pages = randint(50, 400)
        self.cursor.execute('INSERT INTO books('
                            'name,'
                            'price,'
                            'description,'
                            'pages)'
                            'VALUES (?, ?, ?, ?);', (name, price,
                                                     description, pages))
        self.book_id = self.cursor.lastrowid

    def authors(self) -> None:
        first_name = RandGen(RandFirstName).generate(randint(3, 10))
        last_name = RandGen(RandLastName).generate(randint(3, 15))
        birth_date = datetime.datetime.fromtimestamp(
            randint(-2208988800, 946684800)).strftime('%Y-%m-%d %H:%M:%S')
        death_date = datetime.datetime.fromtimestamp(
            randint(-2208988800, 946684800)).strftime('%Y-%m-%d %H:%M:%S')
        information = RandGen(RandWord).generate(randint(10, 20))
        self.cursor.execute('INSERT INTO authors('
                            'first_name,'
                            'last_name,'
                            'birth_date,'
                            'death_date,'
                            'information)'
                            'VALUES (?, ?, ?, ?, ?);',
                            (first_name, last_name, birth_date,
                             death_date, information))
        self.author_id = self.cursor.lastrowid

    def genres(self) -> None:
        name = RandGen(RandWord).generate(randint(3, 10))
        description = RandGen(RandWord).generate(randint(10, 20))
        try:
            self.cursor.execute('INSERT INTO genres('
                                'name,'
                                'description)'
                                'VALUES (?, ?);', (name, description))
            self.genre_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.genres()

    def bankcards(self) -> None:
        number = FakeFactory(providers.BankCardProvider, 1).generate()
        first_name = RandGen(RandFirstName).generate(randint(3, 10))
        last_name = RandGen(RandLastName).generate(randint(3, 15))
        cvc = randint(100, 999)
        period = datetime.datetime.fromtimestamp(
            randint(int(time()), int(time() + 315532800))).strftime('%Y-%m')
        try:
            self.cursor.execute('INSERT INTO bankcards('
                                'number,'
                                'first_name,'
                                'last_name,'
                                'cvc,'
                                'period,'
                                'user_id)'
                                'VALUES (?, ?, ?, ?, ?, ?);', (number, first_name,
                                                               last_name, cvc,
                                                               period,
                                                               self.user_id))
            self.card_id = self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.bankcards()

    def adresses(self) -> None:
        country = RandGen(RandWord).generate(randint(3, 10))
        city = RandGen(RandWord).generate(randint(3, 10))
        street = RandGen(RandWord).generate(randint(3, 10))
        house_number = randint(1, 200)
        postcode = randint(11111, 99999)
        self.cursor.execute('INSERT INTO adresses('
                            'country,'
                            'city,'
                            'street,'
                            'house_number,'
                            'postcode,'
                            'user_id)'
                            'VALUES (?, ?, ?, ?, ?, ?);', (country, city,
                                                           street,
                                                           house_number,
                                                           postcode,
                                                           self.user_id))
        self.adress_id = self.cursor.lastrowid

    def transactions(self) -> None:
        price = uniform(1, 100000)
        self.cursor.execute('INSERT INTO transactions('
                            'basket_id,'
                            'card_id,'
                            'price,'
                            'adress_id)'
                            'VALUES (?, ?, ?, ?);', (self.basket_id,
                                                     self.card_id,
                                                     price, self.adress_id))
        self.transaction_id = self.cursor.lastrowid

    def intermediate_tables(self) -> None:
        self.cursor.execute('INSERT INTO users_roles('
                            'user_id,'
                            'role_id)'
                            'VALUES (?, ?);', (self.user_id, self.role_id))
        self.cursor.execute('INSERT INTO roles_permissions('
                            'role_id,'
                            'permission_id)'
                            'VALUES (?, ?);', (self.role_id,
                                               self.permission_id))
        self.cursor.execute('INSERT INTO books_baskets('
                            'book_id,'
                            'basket_id)'
                            'VALUES (?, ?);', (self.book_id, self.basket_id))
        self.cursor.execute('INSERT INTO books_authors('
                            'book_id,'
                            'author_id)'
                            'VALUES (?, ?);', (self.book_id, self.author_id))
        self.cursor.execute('INSERT INTO books_genres('
                            'book_id,'
                            'genre_id)'
                            'VALUES (?, ?);', (self.book_id, self.genre_id))
