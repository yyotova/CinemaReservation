from cinema_reservation_system.database.db import *


def atomic(method):
    def inner_method(instance, *args, **kwargs):
        session = Session()
        value = method(instance, session, *args, **kwargs)
        session.commit()
        return value
    return inner_method


def atomicmethods(cls):
    for attr, value in vars(cls).items():
        if not attr.startswith('__') and callable(value):
            setattr(cls, attr, atomic(value))
    return cls
