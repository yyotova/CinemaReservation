from cinema_reservation_system.utls.cookies import *
from cinema_reservation_system.config.config_session import SESSION_NAME


def menu():
    print(f'''
    [1] show movies
    [2] show movie projections <movie_id> [<date>]
    [3] make reservation
    [4] cancel reservation
    [5] exit
    [6] help
    ''')


def session_menu():
    menu = f'''
        Welcome {read_cookie(SESSION_NAME).split(",")[0]}:
        [1] Continue
        [2] Log out
        '''
    print(menu)
    return input('Choise:')
