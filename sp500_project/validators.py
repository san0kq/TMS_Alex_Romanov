import re

from errors import (
    UserChoiceError,
    AddNewCompanyError,
    UpdateCompanyError,
    RecordsNumberError,
    EmptyInputError,
)
from data_access import get_all_records


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
    else:
        for row in get_all_records():
            if symbol == row.get('Symbol'):
                raise AddNewCompanyError(f'"{symbol}" already exists in the '
                                         f'table. The symbol must be unique.')


def validate_new_company_name(company_name: str) -> None:
    if not 3 <= len(company_name) <= 50:
        raise AddNewCompanyError(f'The company name bust consist of '
                                 f'3-50 characters. You have entered: '
                                 f'{len(company_name)} characters.')
    else:
        for row in get_all_records():
            if company_name == row.get('Name'):
                raise AddNewCompanyError(f'"{company_name}" already exists in '
                                         f'the table. The name must be '
                                         f'unique.')


def validate_new_company_sector(sector: str) -> bool | None:
    for row in get_all_records():
        if sector == row.get('Sector'):
            return True

    raise AddNewCompanyError(f'The "{sector}" sector does not exist in the '
                             f'table. Please select an existing sector -\n'
                             f'["Consumer Discretionary", "Consumer Staples", '
                             f'"Energy", "Financials",\n"Materials", '
                             f'"Telecommunication Services", "Real Estate", '
                             f'"Industrials", "Utilities",\n"Health Care", '
                             f'"Information Technology"]')


def validate_new_company_price(price: str) -> None:
    if not price.replace('.', '', 1).replace('-', '', 1).isdigit():
        raise AddNewCompanyError('Price must be a digit.')

    elif not (price.count('.') == 1 and 0 <= float(price) <= 1000):
        raise AddNewCompanyError('The number must be a floating-point value '
                                 'and in the range from 0 to 1000')


def validate_company_symbol(company_symbol: str) -> bool | None:
    for row in get_all_records():
        if company_symbol.lower() == row.get('Symbol').lower():
            return True

    raise UpdateCompanyError(f'The "{company_symbol}" symbol does not exist '
                             f'in the table. Please select an existing symbol')


def validate_records_number(records_number: str) -> None:
    if not records_number.isdigit():
        raise RecordsNumberError('Number of records must be digit.')

    elif not 1 <= int(records_number) <= 10000:
        raise RecordsNumberError('Number of records must be in the range '
                                 'from 1 to 10000.')
