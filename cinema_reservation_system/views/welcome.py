import sys
sys.path.append('.')
from cinema_reservation_system.users import UserViews


def welcome():
    command = input('Choose a command:\n  1 - log in\n  2 - sign up\n  3 - menu\n  Input: ')
    user_views = UserViews()

    if command == '1':
        return user_views.login()
    elif command == '2':
        return user_views.signup()
        # call menu
    elif command == '3':
        return True
    else:
        raise ValueError(f'Unknown command {command}.')

# change to index view