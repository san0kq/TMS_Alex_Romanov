from operator import itemgetter
from statistics import mean
from random import randint, uniform

from faker import Faker

from data_access import get_all_records, add_new_records, truncate_data


def find_info_by_name(company_name: str) -> list | str:
    result = []
    for row in get_all_records():
        if company_name.lower() in row.get('Name').lower():
            result.append({
                'Name': row.get('Name'),
                'Symbol': row.get('Symbol'),
                'Sector': row.get('Sector'),
                'Stock price': row.get('Price'),
            }
            )

    return result


def find_info_by_symbol(company_symbol: str) -> list:
    result = []
    for row in get_all_records():
        if company_symbol.lower() == row.get('Symbol').lower():
            result.append({
                'Name': row.get('Name'),
                'Symbol': row.get('Symbol'),
                'Sector': row.get('Sector'),
                'Stock price': row.get('Price'),
            }
            )

    return result


def get_all_companies_by_sector(sector: str) -> list:
    result = []
    for row in get_all_records():
        if sector.lower() == row.get('Sector').lower():
            result.append(row.get('Name'))

    return result


def calculate_average_price() -> float:
    result = []
    for row in get_all_records():
        result.append(float(row.get('Price')))

    return round(mean(result), 2)


def get_top_10_companies() -> list:
    result = []
    for row in get_all_records():
        result.append((row.get('Name'), float(row.get('Price'))))

    result.sort(key=itemgetter(1), reverse=True)

    return result[:10]


def add_new_company(symbol: str,
                    name: str,
                    sector: str,
                    price: str,
                    ) -> None:
    new_company = [{
        'Symbol': symbol,
        'Name': name,
        'Sector': sector,
        'Price': price,
    }]

    add_new_records(data=new_company, mode='a', rest_value='None')


def update_company_name(symbol: str, company_name: str) -> None:
    new_data = []
    for row in get_all_records():
        if symbol.lower() == row.get('Symbol').lower():
            row['Name'] = company_name

        new_data.append(row)
    add_new_records(data=new_data, mode='w')


def delete_company(symbol: str) -> None:
    new_data = []
    for row in get_all_records():
        if symbol.lower() == row.get('Symbol').lower():
            continue
        new_data.append(row)
    add_new_records(data=new_data, mode='w')


def truncate_all() -> str:
    return truncate_data()


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

    add_new_records(data=new_data, mode='w', rest_value='None')
