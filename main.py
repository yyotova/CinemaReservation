import sys

from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.database.create_tables import *

from CinemaReservationSystem.utls.welcome import welcome


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.executescript(CREATE_USERS + CREATE_MOVIES + CREATE_PROJECTION + CREATE_RESERVATION + CREATE_SESSION)
        '''
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_PROJECTION)
        db.cursor.execute(CREATE_RESERVATION)
        db.cursor.execute(CREATE_SESSION)
        '''
        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this

        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def start(self):
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
