from functools import wraps
from operator import itemgetter
from statistics import mean
from random import randint, uniform, choice
from sys import stderr
from time import sleep, time
from typing import Callable, TypeVar, ParamSpec, Any
from string import ascii_uppercase

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
          ) -> Callable[[Callable[P, RT]], Callable[P, Any]]:
    def inner(func: Callable[P, RT]) -> Callable[P, Any]:
        cache_dict = dict()
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            cache_key = (args, tuple(kwargs.values()))
            if cache_key not in cache_dict:
                cache_dict[cache_key] = (func(*args, **kwargs), time())
            else:
                if time() - cache_dict[cache_key][1] > cache_time:
                    cache_dict[cache_key] = (func(*args, **kwargs), time())
            return cache_dict[cache_key][0]
        return wrapper
    return inner


@cache(30)
def find_info_by_name(company_name: str) -> list[dict[str, Any]]:
    return database.read(value=company_name, key='Name')


@cache(30)
def find_info_by_symbol(company_symbol: str) -> list[dict[str, Any]]:
    return database.read(value=company_symbol, key='Symbol')


@cache(30)
def get_all_companies_by_sector(sector: str) -> list[str]:
    return database.read(value=sector, key='Sector')


def calculate_average_price() -> float:
    data = [x[1] for x in database.read(key='Price')]
    return round(mean(data), 2)


def get_top_10_companies() -> list[tuple[str, float]]:
    result = database.read(key='Price')
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
        database.update(symbol=symbol, company_name=company_name)
    except SymbolExistsError as err:
        print(err, file=stderr)
        sleep(0.5)


def delete_company(symbol: str) -> None:
    try:
        database.validate_symbol_not_exists(company_symbol=symbol)
        database.delete(symbol=symbol)
    except SymbolExistsError as err:
        print(err, file=stderr)
        sleep(0.5)


def truncate_all() -> str:
    return database.truncate()


def populate_file_random(records_number: str) -> None:
    new_data = []
    unique_symbol_check = []
    unique_company_check = []
    sectors = ['Consumer Discretionary', 'Consumer Staples', 'Energy',
               'Financials', 'Materials', 'Telecommunication Services',
               'Real Estate', 'Industrials', 'Utilities', 'Health Care',
               'Information Technology']

    fake = Faker()
    for _ in range(int(records_number)):
        while True:
            symbol = ''.join([choice(ascii_uppercase) for _ in
                              range(randint(3, 6))])
            if symbol not in unique_symbol_check:
                break
        while True:
            company_name = fake.company()
            if company_name not in unique_company_check:
                break

        row = {
            'Symbol': symbol,
            'Name': company_name,
            'Sector': sectors[randint(0, 10)],
            'Price': round(uniform(0, 1000), 2),
        }
        unique_symbol_check.append(symbol)
        unique_company_check.append(company_name)

        new_data.append(row)

    database.populate(data=new_data)


def close_db() -> None:
    database.close()
