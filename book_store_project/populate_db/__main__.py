import sys
import os

from providers import RandomValueFromListProvider, gateway_provider
from validators import (
    db_name_validator, 
    records_number_validator, 
    parameters_validator
)
from data_access.dao import (
    UserDAO,
    RoleDAO,
    PermissionDAO,
    BookDAO,
    AuthorDAO,
    GenreDAO,
    AdressDAO,
    TransactionDAO,
    UserRoleDAO,
    RolePermissionDAO,
    BookBasketDAO,
    BookAuthorDAO,
    BookGenreDAO,
)
from factories import (
    UserFactory,
    RoleFactory,
    PermissionFactory,
    BookFactory,
    AuthorFactory,
    GenreFactory,
    AdressFactory,
    TransactionFactory,
    UserRoleFactory,
    RolePermissionFactory,
    BookBasketFactory,
    BookAuthorFactory,
    BookGenreFactory,
)
from rand_gen import (
    RandGen,
    RandWord,
    RandFirstName,
    RandLastName,
    RandEmail,
    RandText,
    RandPhone,
    RandBankCard,
)
from populate_table_command import PopulateTable


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

AVAILABLE_FLAGS = ('-d', '-n')

if __name__ == '__main__':
    config_args = sys.argv[1:]
    parameters_validator(config_args)
    for index in range(0, len(config_args), 2):
        flag = config_args[index]
        if flag not in AVAILABLE_FLAGS:
            raise ValueError('You need to specify the path to the database '
                             'and the number of records. Use the keys "-d" '
                             'and "-n". For example: python populate_db -d '
                             'test.db -n 10.')
        elif flag == '-d':
            db_name = config_args[index + 1]
            db_name_validator(value=db_name)
        elif flag == '-n':
            records_number = config_args[index + 1]
            records_number_validator(value=records_number)
            records_number = int(records_number)

    db_gateway = gateway_provider(db_name=db_name)
    user_dao = UserDAO(db_gateway=db_gateway)
    user_factory = UserFactory(username_provider=RandGen(RandWord),
                               password_provider=RandGen(RandWord),
                               first_name_provider=RandGen(RandFirstName),
                               last_name_provider=RandGen(RandLastName),
                               email_provider=RandGen(RandEmail),
                               phone_provider=RandGen(RandPhone),
                               number_provider=RandGen(RandBankCard)
                               )
    PopulateTable(
        records_number=records_number,
        dao=user_dao,
        fake_factory=user_factory
    ).execute()

    role_dao = RoleDAO(db_gateway=db_gateway)
    role_factory = RoleFactory(name_provider=RandGen(RandWord))
    PopulateTable(
        records_number=records_number,
        dao=role_dao,
        fake_factory=role_factory
    ).execute()

    permission_dao = PermissionDAO(db_gateway=db_gateway)
    permission_factory = PermissionFactory(name_provider=RandGen(RandWord))
    PopulateTable(
        records_number=records_number,
        dao=permission_dao,
        fake_factory=permission_factory
    ).execute()

    book_dao = BookDAO(db_gateway=db_gateway)
    book_factory = BookFactory(
        name_provider=RandGen(RandWord),
        description=RandGen(RandText)
    )
    PopulateTable(
        records_number=records_number,
        dao=book_dao,
        fake_factory=book_factory
    ).execute()

    author_dao = AuthorDAO(db_gateway=db_gateway)
    author_factory = AuthorFactory(
        first_name_provider=RandGen(RandFirstName),
        last_name_provider=RandGen(RandLastName),
        information_provider=RandGen(RandText)
    )
    PopulateTable(
        records_number=records_number,
        dao=author_dao,
        fake_factory=author_factory
    ).execute()

    genre_dao = GenreDAO(db_gateway=db_gateway)
    genre_factory = GenreFactory(
        name_provider=RandGen(RandWord),
        description_provider=RandGen(RandText)
    )
    PopulateTable(
        records_number=records_number,
        dao=genre_dao,
        fake_factory=genre_factory
    ).execute()

    adress_dao = AdressDAO(db_gateway=db_gateway)
    users_list = user_dao.get_ids_list()
    adress_factory = AdressFactory(
        country_provider=RandGen(RandWord),
        city_provider=RandGen(RandWord),
        street_provider=RandGen(RandWord),
        user_id_provider=RandomValueFromListProvider(users_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=adress_dao,
        fake_factory=adress_factory
    ).execute()

    transaction_dao = TransactionDAO(db_gateway=db_gateway)
    adresses_list = adress_dao.get_ids_list()
    baskets_list = user_dao.get_ids_list()
    cards_list = user_dao.get_ids_list()
    transaction_factory = TransactionFactory(
        basket_id_provider=RandomValueFromListProvider(baskets_list),
        card_id_provider=RandomValueFromListProvider(cards_list),
        adress_id_provider=RandomValueFromListProvider(adresses_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=transaction_dao,
        fake_factory=transaction_factory
    ).execute()

    user_role_dao = UserRoleDAO(db_gateway=db_gateway)
    users_list = user_dao.get_ids_list()
    roles_list = role_dao.get_ids_list()
    user_role_factory = UserRoleFactory(
        user_id_provider=RandomValueFromListProvider(users_list),
        role_id_provider=RandomValueFromListProvider(roles_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=user_role_dao,
        fake_factory=user_role_factory
    ).execute()

    role_permission_dao = RolePermissionDAO(db_gateway=db_gateway)
    roles_list = role_dao.get_ids_list()
    permissions_list = permission_dao.get_ids_list()
    role_permission_factory = RolePermissionFactory(
        role_id_provider=RandomValueFromListProvider(roles_list),
        permission_id_provider=RandomValueFromListProvider(permissions_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=role_permission_dao,
        fake_factory=role_permission_factory
    ).execute()

    book_basket_dao = BookBasketDAO(db_gateway=db_gateway)
    books_list = book_dao.get_ids_list()
    baskets_list = user_dao.get_ids_list()
    book_basket_factory = BookBasketFactory(
        book_id_provider=RandomValueFromListProvider(books_list),
        basket_id_provider=RandomValueFromListProvider(baskets_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=book_basket_dao,
        fake_factory=book_basket_factory
    ).execute()

    book_author_dao = BookAuthorDAO(db_gateway=db_gateway)
    books_list = book_dao.get_ids_list()
    authors_list = author_dao.get_ids_list()
    book_author_factory = BookAuthorFactory(
        book_id_provider=RandomValueFromListProvider(books_list),
        author_id_provider=RandomValueFromListProvider(authors_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=book_author_dao,
        fake_factory=book_author_factory
    ).execute()

    book_genre_dao = BookGenreDAO(db_gateway=db_gateway)
    books_list = book_dao.get_ids_list()
    genres_list = genre_dao.get_ids_list()
    book_genre_factory = BookGenreFactory(
        book_id_provider=RandomValueFromListProvider(books_list),
        genre_id_provider=RandomValueFromListProvider(genres_list)
    )
    PopulateTable(
        records_number=records_number,
        dao=book_genre_dao,
        fake_factory=book_genre_factory
    ).execute()
