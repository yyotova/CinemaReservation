from CinemaReservationSystem.database.db import Database


def atomic(method):
    db = Database()

    def inner_method(db, *args, **kwargs):
        return method(db, *args, **kwargs)
    return inner_method(db)
    db.connection.commit()
    db.connection.close()
