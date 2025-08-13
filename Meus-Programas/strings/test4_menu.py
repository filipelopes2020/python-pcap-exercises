import random

def interact_main_menu():
    while True:
        print('\n-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            interact_password_type()
        elif user_choice == '2':
            print('Bye!')
            break
        else:
            print('Please enter a correct value')

