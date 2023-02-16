import csv

from .errors import (
    RecordAlreadyExistsError,
    SectorExistsError,
    SymbolExistsError,
)


def get_all_records() -> list:
    with open('data/sp500.csv', 'r') as file:
        for row in csv.DictReader(file):
            yield row


def add_new_records(data: list, mode: str, rest_value=None) -> None:
    with open('data/sp500.csv', mode) as csv_file:

        fieldnames = ['Symbol', 'Name', 'Sector', 'Price', 'Price/Earnings',
                      'Dividend Yield', 'Earnings/Share', '52 Week Low',
                      '52 Week High', 'Market Cap', 'EBITDA', 'Price/Sales',
                      'Price/Book', 'SEC Filings']

        writer = csv.DictWriter(csv_file,
                                fieldnames=fieldnames,
                                restval=rest_value)
        if mode == 'w':
            writer.writeheader()

        writer.writerows(data)


def truncate_data() -> str:
    with open('data/sp500.csv', 'w') as csv_file:
        return f'All records from the "{csv_file.name}" have been deleted.'


def validate_record_exists(value: str, key: str):
    for row in get_all_records():
        if value == row.get(key):
            raise RecordAlreadyExistsError(f'"{value}" already exists in '
                                           f'the table. The value must be '
                                           f'unique.')


def validate_new_company_sector(sector: str) -> bool | None:
    for row in get_all_records():
        if sector == row.get('Sector'):
            return True

    raise SectorExistsError(f'The "{sector}" sector does not exist.\n'
                            f'Please select an existing sector -\n'
                            f'["Consumer Discretionary", "Consumer Staples", '
                            f'"Energy", "Financials",\n"Materials", '
                            f'"Telecommunication Services", "Real Estate", '
                            f'"Industrials", "Utilities",\n"Health Care", '
                            f'"Information Technology"]')


def validate_symbol_not_exists(company_symbol: str) -> bool | None:
    for row in get_all_records():
        if company_symbol.lower() == row.get('Symbol').lower():
            return True

    raise SymbolExistsError(f'The "{company_symbol}" symbol does not exist '
                            f'in the table. Please select an existing symbol')
