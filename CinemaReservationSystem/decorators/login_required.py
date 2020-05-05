from CinemaReservationSystem.database.session_specific.select_session import SELECT_SESSION
from CinemaReservationSystem.database.db import Database


def login_required(func):
    db = Database()
    user = db.cursor.execute(SELECT_SESSION).fetchone()
    db.connection.commit()
    db.connection.close()

    def inner_func():
        func()
    if user:
        return inner_func()
    else:
        return False
