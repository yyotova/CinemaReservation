import os
from CinemaReservationSystem.config.config_session import SESSION_NAME


def login_required(method):
    def inner_method(*args, **kwargs):
        if os.path.exists(SESSION_NAME):
            return method(*args, **kwargs)

    return inner_method
