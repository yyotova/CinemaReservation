from cinema_reservation_system.database.db import Database


def atomic(method):
    def inner_method(instance, *args, **kwargs):
        db = Database()
        cursor = db.connection.cursor()
        value = method(instance, cursor, *args, **kwargs)
        db.connection.commit()
        db.connection.close()
        return value
    return inner_method


def atomicmethods(cls):
    for attr, value in vars(cls).items():
        if not attr.startswith('__') and callable(value):
            setattr(cls, attr, atomic(value))
    return cls
