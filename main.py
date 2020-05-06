import sys

from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.database.create_tables import *
from CinemaReservationSystem.movies import MovieView
from CinemaReservationSystem.utls import welcome, menu


class Application:
    db = Database()

    @classmethod
    def build(cls):
        cls.db.cursor.executescript(CREATE_USERS + CREATE_MOVIES + CREATE_PROJECTION + CREATE_RESERVATION + CREATE_SESSION)
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

        print('Updated')

    @classmethod
    def start(self):
        welcome()
        menu()
        command = input('Command: ')

        if command == '1':
            movie_view = MovieView()
            movie_view.print_all_movies()


if __name__ == '__main__':
    command = sys.argv[2]
    today = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
        Application.update_projections(date=today)
    elif command == 'insert_data':
        Application.insert_data()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build", "start" and "insert data"')
