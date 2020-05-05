import sys
from database import (CREATE_MOVIES, CREATE_PROJECTION,
    CREATE_RESERVATION, CREATE_SESSION, CREATE_USERS)

from db import DataBase


class Aplication:
    @classmethod
    def build(cls):
        db = DataBase()
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_PROJECTION)
        db.cursor.execute(CREATE_RESERVATION)
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_SESSION)

        db.connection.commit()
        db.connection.close()
        print('The database is build!')


def main():
    command = sys.argv[1]

    if command == 'build':
        Aplication.build()


if __name__ == '__main__':
    main()
