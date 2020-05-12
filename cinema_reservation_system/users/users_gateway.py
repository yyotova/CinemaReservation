from cinema_reservation_system.database.db import Database
import cinema_reservation_system.users.models
from cinema_reservation_system.database.user_specific.user_manipulation import *
from cinema_reservation_system.database.create_tables import *
from cinema_reservation_system.decorators import atomic


class UserGateway:
    def __init__(self):
        self.model = cinema_reservation_system.users.models.UserModel
        self.db = Database()

    @atomic
    def create(self, cursor, *, email, password, salt):
        try:
            cursor.execute(INSERT_USER, (email, password, salt))
            return email
        except Exception as e:
            return e

    @atomic
    def login(self, cursor, *, email, password):
        return cursor.execute(SELECT_USER, (email, password)).fetchone()

    @atomic
    def user(self, cursor, *, email):
        cursor.execute('''
            SELECT id
              FROM users
              WHERE email = (?)
            ''', (email, ))

        return cursor.fetchone()[0]

    @atomic
    def get_salt(self, cursor, salt):
        if cursor.execute(SELECT_SALT, (salt, )):
            return cursor.fetchone()

    @atomic
    def get_user_email(self, cursor, email):
        return cursor.execute(SELECT_USER_EMAIL, (email,)).fetchone()

    @atomic
    def get_user_salt(self, cursor, email):
        return cursor.execute(SELECT_SALT_USER, (email, )).fetchone()[0]
