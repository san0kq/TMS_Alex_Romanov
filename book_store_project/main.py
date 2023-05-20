import sys
import os
from sys import stderr
from time import sleep


from business_logic import UsersData, BookData, AuthorData, TransactionData
from validators import (
    ChoiceValidator,
    id_validator,
    email_validator,
    phone_validator,
    book_name_validator,
)
from errors import UserChoiceError, EmailError, PhoneError, BookError
from data_access.errors import RecordExistsError


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


main_menu = ('1 - users\n2 - books\n3 - authors\n4 - transactions\n5 - exit\n'
             'Your choice: ')
users_menu = ('1 - List of all users\n2 - Get user info\n3 - Delete user\n'
              '4 - Update user email\n5 - Update user phone\nYour choice: ')
books_menu = ('1 - List of all books\n2 - Get book info\n3 - Delete book\n'
              '4 - Update book Name\nYour choice: ')
authors_menu = '1 - List of all authors\n2 - Get author info\nYour choice: '


while True:
    try:
        choice = input(main_menu)
        ChoiceValidator(choice=choice).user_choice()
    except UserChoiceError as err:
        print(err, file=stderr)
        sleep(0.5)
        continue

    if choice == '1':
        try:
            user_choice = input(users_menu)
            ChoiceValidator(choice=user_choice).user_choice()
        except UserChoiceError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

        if user_choice == '1':
            print(UsersData().list())

        elif user_choice == '2':
            try:
                user_id = input('Please, enter user ID: ')
                id_validator(value=user_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(UsersData().user_info(user_id=int(user_id)))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif user_choice == '3':
            try:
                user_id = input('Please, enter user ID you want to delete: ')
                id_validator(choice=user_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(UsersData().delete(user_id=int(user_id)))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif user_choice == '4':
            try:
                user_id = input('Please, enter user ID: ')
                id_validator(value=user_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                email = input('Enter new email: ')
                email_validator(value=email)
            except EmailError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(UsersData().update(user_id=int(user_id),
                                         column='email',
                                         value=email))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif user_choice == '5':
            try:
                user_id = input('Please, enter user ID: ')
                id_validator(value=user_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                phone = input('Enter new phone: ')
                phone_validator(value=phone)
            except PhoneError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(UsersData().update(user_id=int(user_id),
                                         column='phone',
                                         value=phone))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

    elif choice == '2':
        try:
            book_choice = input(books_menu)
            ChoiceValidator(choice=book_choice).book_choice()
        except UserChoiceError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

        if book_choice == '1':
            print(BookData().list())

        elif book_choice == '2':
            try:
                book_id = input('Please, enter book ID: ')
                id_validator(value=book_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(BookData().book_info(book_id=int(book_id)))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif book_choice == '3':
            try:
                book_id = input('Please, enter book ID you want to delete: ')
                id_validator(value=book_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(BookData().delete(book_id=int(book_id)))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif book_choice == '4':
            try:
                book_id = input('Please, enter book ID: ')
                id_validator(value=book_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                book_name = input('Enter new book name: ')
                book_name_validator(value=book_name)
            except BookError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(BookData().update(book_id=int(book_id),
                                        value=book_name))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

    elif choice == '3':
        try:
            author_choice = input(authors_menu)
            ChoiceValidator(choice=author_choice).author_choice()
        except UserChoiceError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

        if author_choice == '1':
            print(AuthorData().list())

        elif author_choice == '2':
            try:
                author_id = input('Please, enter author ID: ')
                id_validator(value=author_id)
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

            try:
                print(AuthorData().author_info(author_id=int(author_id)))
            except RecordExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

    elif choice == '4':
        print(TransactionData().list())

    elif choice == '5':
        break
