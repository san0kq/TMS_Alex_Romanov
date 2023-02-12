import csv
from operator import itemgetter
from statistics import mean
from functools import wraps


def cache_decorator(func):
    @wraps(func)
    def wrapper(*args):
        """
        The first two blocks of conditions are for the last two functions,
        which take only one argument and return only one constant value. After
        "else", there is a block of conditions for the remaining functions with
        two arguments.
        """
        if len(args) == 1 and 'Key' not in wrapper.cache:
            wrapper.cache['Key'] = func(*args)
        elif len(args) == 1:
            return wrapper.cache['Key']
        else:
            cache_key = args[0]
            if cache_key not in wrapper.cache:
                wrapper.cache[cache_key] = func(*args)
            return wrapper.cache[cache_key]
        return wrapper.cache['Key']
    wrapper.cache = dict()
    return wrapper


@cache_decorator
def find_info_by_name(company_name: str, reader: csv.DictReader) -> list | str:
    result = []
    if company_name == '':
        return "You cannot enter an empty string. Please enter something."
    for row in reader:
        if company_name.lower() in row['Name'].lower():
            result.append(row)

    return result


@cache_decorator
def find_info_by_symbol(company_symbol: str, reader: csv.DictReader) -> list:
    result = []
    for row in reader:
        if company_symbol.lower() == row['Symbol'].lower():
            result.append(row)

    return result


@cache_decorator
def get_all_companies_by_sector(sector: str, reader: csv.DictReader) -> list:
    result = []
    for row in reader:
        if sector.lower() == row['Sector'].lower():
            result.append(row['Name'])

    return result


@cache_decorator
def calculate_average_price(reader: csv.DictReader) -> float:
    result = []
    for row in reader:
        result.append(float(row['Price']))

    return round(mean(result), 2)


@cache_decorator
def get_top_10_companies(reader: csv.DictReader) -> list:
    result = []
    for row in reader:
        result.append((row['Name'], float(row['Price'])))

    result.sort(key=itemgetter(1), reverse=True)
    return result[:10]
