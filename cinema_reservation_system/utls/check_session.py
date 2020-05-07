from cinema_reservation_system.utls.cookies import *
from cinema_reservation_system.config.config_session import SESSION_NAME


def check_for_session():
    delete_cookie_after_date(SESSION_NAME)
    if session_exists(SESSION_NAME):
        return True
    return False
