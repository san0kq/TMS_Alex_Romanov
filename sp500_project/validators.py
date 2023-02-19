import re

from errors import (
    UserChoiceError,
    AddNewCompanyError,
    RecordsNumberError,
    EmptyInputError,
)


def validate_user_choice(choice: str) -> None:
    if not choice.isdigit():
        raise UserChoiceError('Choice must be a digit.')

    elif choice not in map(str, range(1, 12)):
        raise UserChoiceError('Choice must be within the range of 1 to 11.')


def validate_empty_input(value: str) -> None:
    if len(value) == 0:
        raise EmptyInputError('You cannot enter an empty string. '
                              'Please enter something.')


def validate_new_company_symbol(symbol: str) -> None:
    if not re.search(r'^[A-Z]{3,6}$', symbol):
        raise AddNewCompanyError('The symbol must consist '
                                 'of 3-6 uppercase Latin letters.')


def validate_new_company_name(company_name: str) -> None:
    if not 3 <= len(company_name) <= 50:
        raise AddNewCompanyError(f'The company name bust consist of '
                                 f'3-50 characters. You have entered: '
                                 f'{len(company_name)} characters.')


def validate_new_company_price(price: str) -> None:
    if not price.replace('.', '', 1).replace('-', '', 1).isdigit():
        raise AddNewCompanyError('Price must be a digit.')

    elif not (price.count('.') == 1 and 0 <= float(price) <= 1000):
        raise AddNewCompanyError('The number must be a floating-point value '
                                 'and in the range from 0 to 1000')


def validate_records_number(records_number: str) -> None:
    if not records_number.isdigit():
        raise RecordsNumberError('Number of records must be digit.')

    elif not 1 <= int(records_number) <= 10000:
        raise RecordsNumberError('Number of records must be in the range '
                                 'from 1 to 10000.')
