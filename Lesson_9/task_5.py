import sys
from time import sleep

from func import (
    find_info_by_name,
    find_info_by_symbol,
    get_all_companies_by_sector,
    calculate_average_price,
    get_top_10_companies,
)

intro = ("1 - Find info by name\n2 - Find info by symbol\n"
         "3 - Get all companies by sector\n4 - Calculate average price\n"
         "5 - Get top 10 companies\n6 - Exit\n"
         "Your choice: ")

while True:
    choice = input(intro)
    if choice == '1':
        company_name = input('Enter the name of company: ')
        print(find_info_by_name(company_name))
    elif choice == '2':
        company_symbol = input('Enter the symbol of company: ')
        print(find_info_by_symbol(company_symbol))
    elif choice == '3':
        company_sector = input('Enter the sector that interests you: ')
        print(get_all_companies_by_sector(company_sector))
    elif choice == '4':
        print(calculate_average_price())
    elif choice == '5':
        print(get_top_10_companies())
    elif choice == '6':
        print('GOODBYE')
        break
    else:
        print('You have entered an incorrect value. Please try again',
              file=sys.stderr)
        sleep(1)
