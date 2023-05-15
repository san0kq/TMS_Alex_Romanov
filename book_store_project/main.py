import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from business_logic import UsersData

main_menu = ('1 - users\n2 - books\n3 - authors\n4 - transactions\n5 - exit\n'
             'Your choice: ')
users_menu = ('1 - List of all users\n2 - Get user info\n3 - Delete user\n'
             '4 - Update user email\n5 - Update user phone\nYour choice: ')
books_menu = ('1 - List of all books\n2 - Get book info\n3 - Delete book\n'
              '4 - Update book Name\nYour choice: ')
authors_menu = '1 - List of all authors\n2 - Get author info\nYour choice: '


while True:
    choice = input(main_menu)
    if choice == '1':
        user_choice = input(users_menu)
        if user_choice == '1':
            print(UsersData().list())
        
        elif user_choice == '2':
            user_id = input('Please, enter user ID: ')
            print(UsersData().user_info(user_id=int(user_id)))

        elif user_choice == '3':
            user_id = input('Please, enter user ID you want to delete: ')
            print(UsersData().delete(user_id=int(user_id)))

        elif user_choice == '4':
            user_id = input('Please, enter user ID: ')
            email = input('Enter new email: ')
            print(UsersData().update(user_id=int(user_id), 
                                     column='email', 
                                     value=email))

        elif user_choice == '5':
            user_id = input('Please, enter user ID: ')
            phone = input('Enter new phone: ')
            print(UsersData().update(user_id=int(user_id),
                                     column='phone',
                                     value = phone))
    
    elif choice == '2':
        book_choice = input(books_menu)
        if book_choice == '1':
            

            

