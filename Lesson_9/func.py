import csv
from operator import itemgetter
from statistics import mean
from functools import wraps
from typing import Iterable, Any, Callable, TypeVar, ParamSpec

RT = TypeVar('RT')
P = ParamSpec('P')


class OpenFileAsDict(object):
    def __init__(self, file_name: str, method: str) -> None:
        self.file = open(file_name, method)

    def __enter__(self) -> Iterable[dict[str, str | float]]:
        return csv.DictReader(self.file)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()


def cache_decorator(func: Callable[..., RT]) -> Callable[..., RT]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)

        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper


@cache_decorator
def find_info_by_name(company_name: str) -> list[dict[str, str | float]] | str:
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
def find_info_by_symbol(company_symbol: str) -> list[dict[str, str | float]]:
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
def get_all_companies_by_sector(sector: str) -> list[str]:
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


def get_top_10_companies() -> list[tuple[str, float]]:
    with OpenFileAsDict('sp500.csv', 'r') as data:
        result = []
        for row in data:
            result.append((row.get('Name'), float(row.get('Price'))))

        result.sort(key=itemgetter(1), reverse=True)
        return result[:10]
