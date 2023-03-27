from functools import wraps
from operator import itemgetter
from statistics import mean
from random import randint, uniform
from sys import stderr
from time import sleep, time
from typing import Callable, TypeVar, ParamSpec, Any

from faker import Faker

from data import (
    RecordAlreadyExistsError,
    SectorExistsError,
    SymbolExistsError,
    db_provider,
    DATABASE_NAME,
    DATABASE_TYPE,
)

database = db_provider(data_name=DATABASE_NAME, data_type=DATABASE_TYPE)

RT = TypeVar('RT')
P = ParamSpec('P')


def cache(cache_time: int = 60
          ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    def inner(func: Callable[..., RT]) -> Callable[..., RT]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            cache_key = (args, tuple(kwargs.values()))
            if cache_key not in wrapper.cache:
                wrapper.cache[cache_key] = (func(*args, **kwargs), time())
            else:
                if time() - wrapper.cache[cache_key][1] > cache_time:
                    wrapper.cache[cache_key] = (func(*args, **kwargs), time())
            return wrapper.cache[cache_key][0]
        wrapper.cache = dict()
        return wrapper
    return inner


@cache(30)
def find_info_by_name(company_name: str) -> list[dict[str, str | float]]:
    result = []
    for row in database.list():
        if company_name.lower() in row.get('Name').lower():
            result.append({
                'Name': row.get('Name'),
                'Symbol': row.get('Symbol'),
                'Sector': row.get('Sector'),
                'Stock price': row.get('Price'),
            }
            )

    return result


@cache(30)
def find_info_by_symbol(company_symbol: str) -> list[dict[str, str | float]]:
    result = []
    for row in database.list():
        if company_symbol.lower() == row.get('Symbol').lower():
            result.append({
                'Name': row.get('Name'),
                'Symbol': row.get('Symbol'),
                'Sector': row.get('Sector'),
                'Stock price': row.get('Price'),
            }
            )

    return result


@cache(30)
def get_all_companies_by_sector(sector: str) -> list[str]:
    result = []
    for row in database.list():
        if sector.lower() == row.get('Sector').lower():
            result.append(row.get('Name'))

    return result


def calculate_average_price() -> float:
    result = []
    for row in database.list():
        result.append(float(row.get('Price')))

    return round(mean(result), 2)


def get_top_10_companies() -> list[tuple[str, float]]:
    result = []
    for row in database.list():
        result.append((row.get('Name'), float(row.get('Price'))))

    result.sort(key=itemgetter(1), reverse=True)

    return result[:10]


def add_new_company(symbol: str,
                    name: str,
                    sector: str,
                    price: str,
                    ) -> None:
    try:
        database.validate_record_exists(value=symbol, key='Symbol')
        database.validate_record_exists(value=name, key='Name')
        database.validate_new_company_sector(sector=sector)

        new_company = [{
            'Symbol': symbol,
            'Name': name,
            'Sector': sector,
            'Price': price,
        }]

        database.create(data=new_company)
    except RecordAlreadyExistsError as err:
        print(err, file=stderr)
        sleep(0.5)
    except SectorExistsError as err:
        print(err, file=stderr)
        sleep(0.5)


def update_company_name(symbol: str, company_name: str) -> None:
    try:
        database.validate_symbol_not_exists(company_symbol=symbol)
        new_data = []
        for row in database.list():
            if symbol.lower() == row.get('Symbol').lower():
                row['Name'] = company_name

            new_data.append(row)
        database.update(data=new_data)
    except SymbolExistsError as err:
        print(err, file=stderr)
        sleep(0.5)


def delete_company(symbol: str) -> None:
    try:
        database.validate_symbol_not_exists(company_symbol=symbol)
        new_data = []
        for row in database.list():
            if symbol.lower() == row.get('Symbol').lower():
                continue
            new_data.append(row)
        database.update(data=new_data)
    except SymbolExistsError as err:
        print(err, file=stderr)
        sleep(0.5)


def truncate_all() -> str:
    return database.delete()


def populate_file_random(records_number: str) -> None:
    new_data = []
    sectors = ['Consumer Discretionary', 'Consumer Staples', 'Energy',
               'Financials', 'Materials', 'Telecommunication Services',
               'Real Estate', 'Industrials', 'Utilities', 'Health Care',
               'Information Technology']

    fake = Faker()
    for _ in range(int(records_number)):
        row = {
            'Symbol': fake.suffix(),
            'Name': fake.company(),
            'Sector': sectors[randint(0, 10)],
            'Price': round(uniform(0, 1000), 2),
        }
        new_data.append(row)

    database.update(data=new_data, rest_value='None')
