import sys
from cinema_reservation_system.database.db import Database
from cinema_reservation_system.database.create_tables import *
from cinema_reservation_system.views.start import start


class Application:
    db = Database()

    @classmethod
    def build(cls):
        cls.db.cursor.executescript(CREATE_USERS + CREATE_MOVIES + CREATE_PROJECTION + CREATE_RESERVATION)
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
