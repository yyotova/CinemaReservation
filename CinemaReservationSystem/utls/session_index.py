from CinemaReservationSystem.utls.cookies import *
from CinemaReservationSystem.config.config_session import SESSION_NAME


def check_for_session():
    delete_cookie_after_date(SESSION_NAME)
    if session_exists(SESSION_NAME):
        return True
    return False


def session_menu():
    menu = f'''
        Welcome {read_cookie(SESSION_NAME).split(",")[0]}:
        [1] Continue
        [2] Log out
        '''
    print(menu)
    return input('Choise:')
