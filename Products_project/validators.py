import re

from errors import UserChoiceError, NamingError, CategoryExistsError


def validate_user_choice(choice: str) -> None:
    if not choice.isdigit():
        raise UserChoiceError('Choice must be a digit.')

    elif choice not in map(str, range(1, 9)):
        raise UserChoiceError('Choice must be within the range of 1 to 8.')


def validate_category_name(category_name: str) -> None:
    if not 0 < len(category_name) < 15:
        raise NamingError('The length of the category name should be '
                          'from 1 to 15.')


def validate_product_name(product_name: str) -> None:
    if not 0 < len(product_name) < 30:
        raise NamingError('The length of the product name should be '
                          'from 1 to 30.')


def validate_id(product_id: str) -> None:
    if not product_id.isdigit():
        raise ValueError('ID must be a positive integer.')


def validate_parameter_name(parameter_name: str) -> None:
    if not 0 < len(parameter_name) < 10:
        raise NamingError('The length of the parameter name should be '
                          'from 1 to 10.')


def validate_parameter_value(parameter: str) -> None:
    if not 0 < len(parameter) < 50:
        raise NamingError('The length of the parameter should be '
                          'from 1 to 50.')


def validate_category_exists(category_name: str, categories: str) -> None:
    if category_name not in categories:
        raise CategoryExistsError(f'The category "{category_name}" is not in '
                                  f'the list of categories. First, add it or '
                                  f'select from the existing ones.')


def validate_quantity(quantity: str) -> None:
    if not quantity.isdigit():
        raise ValueError('Quantity must be a positive digit.')

    if not int(quantity) > 0:
        raise ValueError('Quantity must be > 0.')


def validate_price(price: str) -> None:
    price_val = price.replace('.', '', 1)
    if not price_val.isdigit():
        raise ValueError('Price must be a integer or float.')
    if not int(price_val) > 0:
        raise ValueError('Price must be > 0.')


def validate_date(date: str) -> None:
    if not re.search(
            r'^(|\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]))$',
            date):
        raise ValueError('Invalid date. The date should be in the format: '
                         'YYYY-MM-DD.')
