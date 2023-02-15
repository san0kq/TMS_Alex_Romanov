import csv


def get_all_records() -> list:
    with open('sp500.csv', 'r') as file:
        return list(csv.DictReader(file))


def add_new_records(data: list, mode: str, rest_value=None) -> None:
    with open('sp500.csv', mode) as csv_file:

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
    with open('sp500.csv', 'w') as csv_file:
        return f'All records from the "{csv_file.name}" have been deleted.'
