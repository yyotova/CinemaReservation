from CinemaReservationSystem.users.views import UserViews


def welcome():
    print('Welcome to HackCinema!')
    command = input('Choose a command:\n  1 - log in\n  2 - sign up\n  3 - menu\n  Input: ')
    user_views = UserViews()

    if command == '1':
        return user_views.login()
    elif command == '2':
        return user_views.signup()
    elif command == '3':
        return True
    else:
        raise ValueError(f'Unknown command {command}.')
