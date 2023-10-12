from sys import stderr
from time import sleep

from errors import (
    UserChoiceError,
    AddNewCompanyError,
    RecordsNumberError,
    EmptyInputError,
)
from business_logic import (
    find_info_by_name,
    find_info_by_symbol,
    get_all_companies_by_sector,
    calculate_average_price,
    get_top_10_companies,
    add_new_company,
    update_company_name,
    delete_company,
    truncate_all,
    populate_file_random,
    close_db,
)
from validators import (
    validate_user_choice,
    validate_new_company_name,
    validate_new_company_symbol,
    validate_new_company_price,
    validate_empty_input,
    validate_records_number,
)

intro = (
    "1 - Find info by name\n2 - Find info by symbol\n"
    "3 - Get all companies by sector\n4 - Calculate average price\n"
    "5 - Get top 10 companies\n6 - Add new company\n"
    "7 - Update company name\n8 - Delete company\n9 - Truncate all\n"
    "10 - Populate file with random data\n11 - Exit\nYour choice: "
)

while True:
    choice = input(intro)
    try:
        validate_user_choice(choice=choice)
    except UserChoiceError as err:
        print(err, file=stderr)
        sleep(0.5)
        continue

    if choice == '1':
        try:
            company_name = input('Enter the name of company: ')
            validate_empty_input(value=company_name)
            print(find_info_by_name(company_name=company_name))
        except EmptyInputError as err:
            print(err, file=stderr)
            sleep(0.5)

    elif choice == '2':
        try:
            company_symbol = input('Enter the symbol of company: ')
            validate_empty_input(value=company_symbol)
            print(find_info_by_symbol(company_symbol=company_symbol))
        except EmptyInputError as err:
            print(err, file=stderr)
            sleep(0.5)

    elif choice == '3':
        try:
            sector = input('Enter the sector that interests you: ')
            validate_empty_input(value=sector)
            print(get_all_companies_by_sector(sector=sector))
        except EmptyInputError as err:
            print(err, file=stderr)
            sleep(0.5)

    elif choice == '4':
        print(calculate_average_price())

    elif choice == '5':
        print(get_top_10_companies())

    elif choice == '6':
        print('Enter the date of the new company.')
        try:
            company_symbol = input('Symbol: ')
            validate_new_company_symbol(symbol=company_symbol)
            company_name = input('Name: ')
            validate_new_company_name(company_name=company_name)
            sector = input('Sector: ')
            price = input('Price: ')
            validate_new_company_price(price=price)

            add_new_company(symbol=company_symbol,
                            name=company_name,
                            sector=sector,
                            price=price,
                            )
        except AddNewCompanyError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

    elif choice == '7':
        try:
            symbol = input('Enter the symbol of company to update: ')
            new_company_name = input('Enter the new name of company: ')
            validate_new_company_name(company_name=new_company_name)
            update_company_name(symbol=symbol, company_name=new_company_name)
        except AddNewCompanyError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

    elif choice == '8':
        symbol = input('Enter the symbol of company to delete: ')
        delete_company(symbol=symbol)

    elif choice == '9':
        warning = input('Are you sure you want to delete the file? [YES/NO] ')
        if warning == 'YES':
            print(truncate_all())
        else:
            continue

    elif choice == "10":
        try:
            records_number = input('How many records do you want '
                                   'to generate? ')
            validate_records_number(records_number=records_number)
            populate_file_random(records_number=records_number)
        except RecordsNumberError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

    elif choice == '11':
        close_db()
        print('GOODBYE')
        break
