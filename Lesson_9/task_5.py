import sys
from time import sleep

from func import OpenFileAsTuple, find_info_by_name, find_info_by_symbol, \
    get_all_companies_by_sector, calculate_average_price, get_top_10_companies

intro = """1 - Find info by name
2 - Find info by symbol
3 - Get all companies by sector
4 - Calculate average price
5 - Get top 10 companies
6 - Exit
Your choice: """

with OpenFileAsTuple('sp500.csv', 'r') as csv_file:

    while True:
        choice = input(intro)
        if choice == '1':
            company_name = input('Enter the name of company: ')
            print(find_info_by_name(company_name, csv_file))
        elif choice == '2':
            company_symbol = input('Enter the symbol of company: ')
            print(find_info_by_symbol(company_symbol, csv_file))
        elif choice == '3':
            company_sector = input('Enter the sector that interests you: ')
            print(get_all_companies_by_sector(company_sector, csv_file))
        elif choice == '4':
            print(calculate_average_price(csv_file))
        elif choice == '5':
            print(get_top_10_companies(csv_file))
        elif choice == '6':
            print('GOODBYE')
            break
        else:
            print('You have entered an incorrect value. Please try again',
                  file=sys.stderr)
            sleep(1)
