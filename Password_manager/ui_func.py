from sys import stderr
from time import sleep

from business_logic import PasswordManager, Code, ExportPasswords
from data import IdentifierExistsError
from validators import validate_user_choice

choices = '1. Add a new password\n2. Get the list of passwords\n' \
          '3. Get a password.\n4. Delete a password.\n' \
          '5. Export all passwords.\n6. Exit.\nYour choice: '


def main() -> None:
    check_code = Code()
    check_code()
    pass_manager = PasswordManager()
    while True:
        try:
            choice = input(choices)
            validate_user_choice(choice=choice)
        except ValueError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

        if choice == '1':
            try:
                pass_manager.identifier = input('Enter password identifier '
                                                '(e.g. Instagram): ')
                pass_manager.password = input('Enter your password: ')
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            pass_manager.add_new_password()

        elif choice == '2':
            print(pass_manager.get_identifiers_list())

        elif choice == '3':
            try:
                pass_manager.identifier = input('Enter password identifier: ')
                print(pass_manager.get_password())
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            except IdentifierExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '4':
            try:
                pass_manager.identifier = input('Enter password identifier: ')
                print(pass_manager.delete_password())
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            except IdentifierExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '5':
            try:
                file_name = input('Enter file name: ')
                export = ExportPasswords(file_name=file_name)
                print(export())
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '6':
            break
