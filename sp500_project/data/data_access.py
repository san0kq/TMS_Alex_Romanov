import csv
import json
import sqlite3
from typing import Union, Generator, Optional, Any, List

from .errors import (
    RecordAlreadyExistsError,
    SectorExistsError,
    SymbolExistsError,
)


def db_provider(
        data_name: str,
        data_type: str) -> Union['Sp500Json', 'Sp500csv', 'Sp500Sqlite']:
    if data_type == '.csv':
        return Sp500csv(data_name=data_name, data_type=data_type)
    elif data_type == '.json':
        return Sp500Json(data_name=data_name, data_type=data_type)
    elif data_type == '.db':
        return Sp500Sqlite(data_name=data_name, data_type=data_type)


class FileDB:
    def __init__(self, data_name: str, data_type: str) -> None:
        self.data_name = data_name
        self.data_type = data_type
        self.database = self.data_name + self.data_type

    def list(self) -> Optional[Generator[dict[str, Any], None, None]]:
        with open(self.database, 'r') as file:
            if self.data_type == '.csv':
                for row in csv.DictReader(file):
                    yield row

            elif self.data_type == '.json':
                for row in json.load(file):
                    yield row

            elif self.data_type == '.db':
                pass

    def read(self, key: str, value: str = None) -> List[dict[str, Any] | Any]:
        result = []
        for row in self.list():
            if key != 'Price':
                if value.lower() in row[key].lower():
                    if key != 'Sector':
                        result.append({
                            'Name': row.get('Name'),
                            'Symbol': row.get('Symbol'),
                            'Sector': row.get('Sector'),
                            'Stock price': row.get('Price'),
                        }
                        )
                    else:
                        result.append(row['Name'])
            else:
                result.append((row['Name'], float(row['Price'])))

        return result

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
            if company_symbol.lower() == row['Symbol'].lower():
                return True

        raise SymbolExistsError(
            f'The "{company_symbol}" symbol does not exist '
            f'in the table. Please select an existing symbol')

    def close(self) -> None:
        pass


class Sp500csv(FileDB):
    def create(self, data: list[dict[str, Any]]) -> None:
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

    def update(self, symbol: str, company_name: str) -> None:
        new_data = []
        for row in self.list():
            if symbol.lower() == row['Symbol'].lower():
                row['Name'] = company_name

            new_data.append(row)
        with open(self.database, 'w') as csv_file:
            fieldnames = ['Symbol', 'Name', 'Sector', 'Price',
                          'Price/Earnings',
                          'Dividend Yield', 'Earnings/Share', '52 Week Low',
                          '52 Week High', 'Market Cap', 'EBITDA',
                          'Price/Sales',
                          'Price/Book', 'SEC Filings']

            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    restval=None)
            writer.writeheader()
            writer.writerows(new_data)

    def delete(self, symbol: str) -> None:
        new_data = []
        for row in self.list():
            if symbol.lower() == row['Symbol'].lower():
                continue
            new_data.append(row)
        with open(self.database, 'w') as csv_file:
            fieldnames = ['Symbol', 'Name', 'Sector', 'Price',
                          'Price/Earnings',
                          'Dividend Yield', 'Earnings/Share', '52 Week Low',
                          '52 Week High', 'Market Cap', 'EBITDA',
                          'Price/Sales',
                          'Price/Book', 'SEC Filings']

            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    restval=None)
            writer.writeheader()
            writer.writerows(new_data)

    def truncate(self) -> str:
        with open(self.database, 'w') as csv_file:
            return f'All records from the "{csv_file.name}" have been deleted.'

    def populate(self, data: list[dict[str, Any]]) -> None:
        with open(self.database, 'w') as csv_file:
            fieldnames = ['Symbol', 'Name', 'Sector', 'Price',
                          'Price/Earnings',
                          'Dividend Yield', 'Earnings/Share', '52 Week Low',
                          '52 Week High', 'Market Cap', 'EBITDA',
                          'Price/Sales',
                          'Price/Book', 'SEC Filings']

            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    restval='None')
            writer.writeheader()
            writer.writerows(data)


class Sp500Json(FileDB):
    def create(self, data: list[dict[str, Any]]) -> None:
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
            symbol: str,
            company_name: Optional[str] = None) -> None:
        new_data = []
        for row in self.list():
            if symbol.lower() == row['Symbol'].lower():
                row['Name'] = company_name

            new_data.append(row)
        with open(self.database, 'w') as file:
            json.dump(new_data, file, indent=2)

    def delete(self, symbol: str) -> None:
        self.update(symbol=symbol)

    def truncate(self) -> str:
        with open(self.database, 'w') as file:
            return f'All records from the "{file.name}" have been deleted.'

    def populate(self, data: list[dict[str, Any]]) -> None:
        with open(self.database, 'w') as file:
            json.dump(data, file, indent=2)


class Sp500Sqlite(FileDB):
    def __init__(self, data_name: str, data_type: str) -> None:
        super().__init__(data_name=data_name, data_type=data_type)
        self.connector = sqlite3.connect(self.database)
        self.cursor = self.connector.cursor()

    def create(self, data: list[dict[str, Any]]) -> None:
        self.cursor.execute('INSERT INTO companies('
                            'symbol,'
                            'name,'
                            'sector,'
                            'price) VALUES(?, ?, ?, ?);', (data[0]['Symbol'],
                                                           data[0]['Name'],
                                                           data[0]['Sector'],
                                                           data[0]['Price'],
                                                           ))
        self.connector.commit()

    def read(self, key: str, value: str = None) -> list[dict[str, Any] | Any]:
        result = []
        if key == 'Name':
            self.cursor.execute("SELECT * FROM companies WHERE LOWER(name) "
                                "LIKE ?;", (f'%{value}%', ))
        elif key == 'Symbol':
            self.cursor.execute("SELECT * FROM companies WHERE LOWER(symbol) "
                                "LIKE ?;", (f'%{value}%',))
        if key == 'Name' or key == 'Symbol':
            results = self.cursor.fetchall()
            for record in results:
                result.append({
                    'Name': record[1],
                    'Symbol': record[0],
                    'Sector': record[3],
                    'Price': record[4],
                })

        if key == 'Sector':
            self.cursor.execute(
                "SELECT name FROM companies WHERE LOWER(sector) " 
                "LIKE ?;", (f'%{value}%',))
            results = self.cursor.fetchall()
            for name in results:
                result.append(name[0])

        elif key == 'Price':
            self.cursor.execute('SELECT name, price FROM companies;')
            result = self.cursor.fetchall()

        return result

    def update(self, symbol: str, company_name: str) -> None:
        self.cursor.execute('UPDATE companies SET name = ? WHERE symbol = ?;',
                            (company_name, symbol))
        self.connector.commit()

    def delete(self, symbol: str) -> None:
        self.cursor.execute('DELETE FROM companies WHERE symbol = ?;',
                            (symbol, ))
        self.connector.commit()

    def truncate(self) -> str:
        self.cursor.execute('DELETE FROM companies;')
        self.connector.commit()
        return f'All records from the "{self.database}" have been deleted.'

    def populate(self, data: list[dict[str, Any]]) -> None:
        self.cursor.execute('DELETE FROM companies;')
        for row in data:
            self.cursor.execute('INSERT INTO companies('
                                'symbol,'
                                'name,'
                                'sector,'
                                'price) VALUES (?, ?, ?, ?);',
                                (row['Symbol'], row['Name'], row['Sector'],
                                 row['Price'],
                                 ))
        self.connector.commit()

    def validate_record_exists(self, value: str, key: str) -> None:
        if key == 'Symbol':
            self.cursor.execute('SELECT * FROM companies WHERE symbol = ?;',
                                (value, ))
        elif key == 'Name':
            self.cursor.execute('SELECT * FROM companies WHERE name = ?;',
                                (value, ))
        if self.cursor.fetchone():
            raise RecordAlreadyExistsError(f'"{value}" already exists in '
                                           f'the table. The value must be '
                                           f'unique.')

    def validate_new_company_sector(self, sector: str) -> Optional[bool]:
        self.cursor.execute('SELECT * FROM sectors WHERE name = ?;',
                            (sector, ))
        if self.cursor.fetchone():
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
        self.cursor.execute('SELECT * FROM companies WHERE '
                            'LOWER(symbol) = LOWER(?);', (company_symbol, ))
        if self.cursor.fetchone():
            return True

        raise SymbolExistsError(
            f'The "{company_symbol}" symbol does not exist '
            f'in the table. Please select an existing symbol')

    def close(self) -> None:
        self.connector.close()
