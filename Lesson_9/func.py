import csv
from operator import itemgetter
from statistics import mean
from functools import wraps


class OpenFileAsDict(object):
    def __init__(self, file_name, method):
        self.file = open(file_name, method)

    def __enter__(self):
        return csv.DictReader(self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def cache_decorator(func):
    @wraps(func)
    def wrapper(*args):
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)

        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper


@cache_decorator
def find_info_by_name(company_name: str) -> list | str:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        if company_name == '':
            return "You cannot enter an empty string. Please enter something."
        for row in data:
            if company_name.lower() in row.get('Name').lower():
                result.append({
                    'Name': row.get('Name'),
                    'Symbol': row.get('Symbol'),
                    'Sector': row.get('Sector'),
                    'Stock price': row.get('Price'),
                }
                )

        return result


@cache_decorator
def find_info_by_symbol(company_symbol: str) -> list:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        for row in data:
            if company_symbol.lower() == row.get('Symbol').lower():
                result.append({
                    'Name': row.get('Name'),
                    'Symbol': row.get('Symbol'),
                    'Sector': row.get('Sector'),
                    'Stock price': row.get('Price'),
                }
                )
        return result


@cache_decorator
def get_all_companies_by_sector(sector: str) -> list:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        for row in data:
            if sector.lower() == row.get('Sector').lower():
                result.append(row.get('Name'))

        return result


def calculate_average_price() -> float:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        for row in data:
            result.append(float(row.get('Price')))

        return round(mean(result), 2)


def get_top_10_companies() -> list:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        for row in data:
            result.append((row.get('Name'), float(row.get('Price'))))

        result.sort(key=itemgetter(1), reverse=True)
        return result[:10]
