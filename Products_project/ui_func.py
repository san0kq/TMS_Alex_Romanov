from sys import stderr
from time import sleep

from errors import UserChoiceError, NamingError, CategoryExistsError
from validators import validate_user_choice, validate_quantity, validate_id
from business_logic import CreateStatistics, Category, Product


choices = '1. Add a new category\n2. Add a new product\n3. Delete a product' \
          '\n4. Get a list of all products in stock\n5. Get a product by ID' \
          '\n6. Place an order\n7. Get statistics\n8. Stop the program.\n' \
          'Your choice: '


def main():
    while True:
        try:
            choice = input(choices)
            validate_user_choice(choice=choice)
        except UserChoiceError as err:
            print(err, file=stderr)
            sleep(0.5)
            continue

        if choice == '1':
            category_name = input('Enter the category name: ').strip()
            try:
                new_category = Category(category_name=category_name)
                print('Please enter the required parameters one by one. '
                      'The maximum number of parameters in one category is 10.'
                      ' If you have finished entering the parameters, '
                      'enter "stop".')
                new_category()
            except NamingError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '2':
            print('Enter the name of the category from the options below:')
            print('------------------------------------------------------')
            categories = Category()
            print(categories.categories_read())
            print('------------------------------------------------------')
            category_name = input()
            product_name = input('Enter a product name: ')
            quantity = input('Enter the quantity of the product: ')
            price = input('Enter the price of the product: ')
            try:
                product = Product(
                    product_name=product_name,
                    category_name=category_name,
                    quantity=quantity,
                    price=price
                )
            except NamingError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            try:
                product()
            except CategoryExistsError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '3':
            product_id = input('Enter the ID of the product you want to '
                               'delete: ')
            product = Product()
            product.delete_product(product_id=product_id)

        elif choice == '4':
            product_category = input('Enter the category of products you '
                                     'are interested in: ')
            try:
                if product_category != '':
                    product = Product(category_name=product_category)
                else:
                    product = Product()

                min_date = input('Enter the minimum date of product addition '
                                 '(YYYY-MM-DD): ')
                max_date = input('Enter the maximum date of product addition '
                                 '(YYYY-MM-DD): ')

                print(product.get_products_list(
                    min_date=min_date,
                    max_date=max_date,
                ))
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            except NamingError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '5':
            product_id = input('Enter the ID of the product you want '
                               'to retrieve: ')
            product = Product()
            try:
                print(product.get_product(product_id=product_id))
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '6':
            try:
                products_id = dict()
                print('Enter the product ID that you are interested in, along '
                      'with its quantity. When you are finished placing your '
                      'order, type the word "stop".')
                while True:
                    product_id = input('Product ID: ')
                    if product_id == 'stop':
                        break
                    validate_id(product_id=product_id)
                    quantity = input(f'Quantity of the product with ID '
                                     f'{product_id}: ')
                    if quantity == 'stop':
                        break
                    validate_quantity(quantity=quantity)
                    products_id[product_id] = int(quantity)
                product = Product()
                print(product.products_order(products_id=products_id))
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue

        elif choice == '7':
            min_date = input('Enter the minimum date from which you want '
                             'to get the statistics (YYYY-MM-DD): ')
            max_date = input('Enter the maximum date from which you want '
                             'to get the statistics (YYYY-MM-DD): ')
            try:
                statistics = CreateStatistics(
                    min_date=min_date,
                    max_date=max_date
                )
            except ValueError as err:
                print(err, file=stderr)
                sleep(0.5)
                continue
            statistics()

        elif choice == '8':
            break
