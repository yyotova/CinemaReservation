import os
# from CinemaReservationSystem.utls.cookies import *
from CinemaReservationSystem.config.config_session import SESSION_NAME


def login_required(method):

    def inner_method(*args, **kwargs):
        return method(*args, **kwargs)
    if os.path.exists(SESSION_NAME):
        return inner_method
    else:
        raise Exception("no user")
