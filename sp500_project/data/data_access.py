import csv
import json
from typing import Union, Generator, Optional

from .errors import (
    RecordAlreadyExistsError,
    SectorExistsError,
    SymbolExistsError,
)


def db_provider(
        data_name: str,
        data_type: str) -> Optional[Union['Sp500Json', 'Sp500csv']]:
    if data_type == '.csv':
        return Sp500csv(data_name, data_type)
    elif data_type == '.json':
        return Sp500Json(data_name, data_type)
    else:
        return None


class FileDB:
    def __init__(self, data_name: str, data_type: str) -> None:
        self.data_name = data_name
        self.data_type = data_type
        self.database = self.data_name + self.data_type

    def list(self) -> Generator[dict[str, str | float], None, None]:
        with open(self.database, 'r') as file:
            if self.data_type == '.csv':
                for row in csv.DictReader(file):
                    yield row

            elif self.data_type == '.json':
                for row in json.load(file):
                    yield row

    def validate_record_exists(self, value: str, key: str) -> None:
        for row in self.list():
            if value == row.get(key):
                raise RecordAlreadyExistsError(f'"{value}" already exists in '
                                               f'the table. The value must be '
                                               f'unique.')

    def validate_new_company_sector(self, sector: str) -> Optional[bool]:
        for row in self.list():
            if sector == row.get('Sector'):
                return True

        raise SectorExistsError(f'The "{sector}" sector does not exist.\n'
                                f'Please select an existing sector -\n'
                                f'["Consumer Discretionary", '
                                f'"Consumer Staples", "Energy", "Financials",'
                                f'\n"Materials", "Telecommunication Services",'
                                f' "Real Estate", "Industrials", "Utilities",'
                                f'\n"Health Care", "Information Technology"]'
                                )

    def validate_symbol_not_exists(
            self,
            company_symbol: str) -> Optional[bool]:
        for row in self.list():
            if company_symbol.lower() == row.get('Symbol').lower():
                return True

        raise SymbolExistsError(
            f'The "{company_symbol}" symbol does not exist '
            f'in the table. Please select an existing symbol')


class Sp500csv(FileDB):
    def create(self, data: list[dict[str, str | int | float]]) -> None:
        with open(self.database, 'a') as csv_file:
            fieldnames = ['Symbol', 'Name', 'Sector', 'Price',
                          'Price/Earnings',
                          'Dividend Yield', 'Earnings/Share', '52 Week Low',
                          '52 Week High', 'Market Cap', 'EBITDA',
                          'Price/Sales',
                          'Price/Book', 'SEC Filings']

            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    restval='None')
            writer.writerows(data)

    def update(
            self,
            data: list[dict[str, str | int | float]],
            rest_value: Optional[str] = None) -> None:
        with open(self.database, 'w') as csv_file:
            fieldnames = ['Symbol', 'Name', 'Sector', 'Price',
                          'Price/Earnings',
                          'Dividend Yield', 'Earnings/Share', '52 Week Low',
                          '52 Week High', 'Market Cap', 'EBITDA',
                          'Price/Sales',
                          'Price/Book', 'SEC Filings']

            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    restval=rest_value)
            writer.writeheader()
            writer.writerows(data)

    def delete(self) -> str:
        with open(self.database, 'w') as csv_file:
            return f'All records from the "{csv_file.name}" have been deleted.'


class Sp500Json(FileDB):
    def create(self, data: list[dict[str, str | int | float]]) -> None:
        with open(self.database, 'r') as file:
            json_data = json.load(file)
        result = {
            'Symbol': data[0]['Symbol'],
            'Name': data[0]['Name'],
            'Sector': data[0]['Sector'],
            'Price': data[0]['Price'],
            'Price/Earnings': 'None',
            'Dividend Yield': 'None',
            'Earnings/Share': 'None',
            '52 Week Low': 'None',
            '52 Week High': 'None',
            'Market Cap': 'None',
            'EBITDA': 'None',
            'Price/Sales': 'None',
            'Price/Book': 'None',
            'SEC Filings': 'None',
        }
        json_data.append(result)

        with open(self.database, 'w') as file:
            json.dump(json_data, file, indent=2)

    def update(
            self,
            data: list[dict[str, str | int | float]],
            rest_value: Optional[str] = None) -> None:
        with open(self.database, 'w') as file:
            json.dump(data, file, indent=2)

    def delete(self) -> str:
        with open(self.database, 'w') as file:
            return f'All records from the "{file.name}" have been deleted.'
