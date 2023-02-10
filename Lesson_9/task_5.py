import csv
import sys
from time import sleep

import func

intro = """1 - Find info by name
2 - Find info by symbol
3 - Get all companies by sector
4 - Calculate average price
5 - Get top 10 companies
6 - Exit
Your choice: """

while True:
    choice = input(intro)
    if choice == '1':
        csv_file = open('sp500.csv')
        reader = csv.DictReader(csv_file)
        company_name = input('Enter the name of company: ')
        print(func.find_info_by_name(company_name, reader))
        csv_file.close()
    elif choice == '2':
        csv_file = open('sp500.csv')
        reader = csv.DictReader(csv_file)
        company_symbol = input('Enter the symbol of company: ')
        print(func.find_info_by_symbol(company_symbol, reader))
        csv_file.close()
    elif choice == '3':
        csv_file = open('sp500.csv')
        reader = csv.DictReader(csv_file)
        company_sector = input('Enter the sector that interests you: ')
        print(func.get_all_companies_by_sector(company_sector, reader))
        csv_file.close()
    elif choice == '4':
        csv_file = open('sp500.csv')
        reader = csv.DictReader(csv_file)
        print(func.calculate_average_price(reader))
        csv_file.close()
    elif choice == '5':
        csv_file = open('sp500.csv')
        reader = csv.DictReader(csv_file)
        print(func.get_top_10_companies(reader))
        csv_file.close()
    elif choice == '6':
        print('GOODBYE')
        break
    else:
        print('You have entered an incorrect value. Please try again',
              file=sys.stderr)
        sleep(1)
