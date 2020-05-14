import sys
from cinema_reservation_system.database.db import *
from cinema_reservation_system.users.models import User
from cinema_reservation_system.reservations.models import Reservation
from cinema_reservation_system.movies.models import Movie, Projection
from cinema_reservation_system.views.start import start
from cinema_reservation_system.utls.delete_old_projections import delete_passed_projection


class Application:

    @classmethod
    def build(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def update_projections(cls, *, date):
        delete_passed_projection(date=date)

    @classmethod
    def start(self):
        start()


if __name__ == '__main__':
    command = sys.argv[2]
    today = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.update_projections(date=today)
        Application.start()
    elif command == 'insert_data':
        Application.insert_data()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build", "start" and "insert data"')
