import sys

from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.database.create_tables import *
from CinemaReservationSystem.movies import MovieView
from CinemaReservationSystem.utls import welcome, menu
from CinemaReservationSystem.utls.cookies import *
from CinemaReservationSystem.config.config_session import SESSION_NAME
from CinemaReservationSystem.reservations import ReservationView


class Application:
    db = Database()

    @classmethod
    def build(cls):
        cls.db.cursor.executescript(CREATE_USERS + CREATE_MOVIES + CREATE_PROJECTION + CREATE_RESERVATION)
        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this
        cls.db.connection.commit()
        cls.db.connection.close()
        print('Done.')

    @classmethod
    def insert_data(cls):
        cls.db.insert_data()
        cls.db.connection.commit()
        cls.db.connection.close()

    @classmethod
    def update_projections(cls, *, date):
        cls.db.delete_passed_projection(date=date)
        cls.db.connection.commit()
        cls.db.connection.close()
        print('Updated')

    @classmethod
    def start(self):
        if welcome():
            exit = False

            while not exit:
                menu()
                command = input('Command: ')
                if command == '1':
                    movie_view = MovieView()
                    movie_view.print_all_movies()

                elif command == '2':
                    movie_view = MovieView()
                    movie_id = input('Enter movie_id: ')
                    date = input('Enter date(optional): ')
                    movie_view.print_movie_projections(movie_id=movie_id, date=date)
                elif command == '3':
                    reservation_view = ReservationView()
                    reservation_view.make_reservation()
                    reservation_view.print_spots()
                    email = read_cookie(SESSION_NAME)
                    reservation_view.choose_seat(email=email)
                elif command == 'exit':
                    exit = True
                    delete_cookie(SESSION_NAME)


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
