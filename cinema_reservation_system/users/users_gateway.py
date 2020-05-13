from cinema_reservation_system.database.db import Database
import cinema_reservation_system.users.models
from cinema_reservation_system.database.user_specific.user_manipulation import *
from cinema_reservation_system.database.create_tables import *
from cinema_reservation_system.decorators import atomicmethods


@atomicmethods
class UserGateway:
    def __init__(self):
        self.model = cinema_reservation_system.users.models.UserModel
        self.db = Database()

    def create(self, cursor, *, email, password, salt):
        try:
            # session.add(class)
            cursor.execute(INSERT_USER, (email, password, salt))
            return email
        except Exception as e:
            return e

    def login(self, cursor, *, email, password):
        return cursor.execute(SELECT_USER, (email, password)).fetchone()

    def user(self, cursor, *, email):
        cursor.execute('''
            SELECT id
              FROM users
              WHERE email = (?)
            ''', (email, ))

        return cursor.fetchone()[0]

    def get_salt(self, cursor, salt):
        if cursor.execute(SELECT_SALT, (salt, )):
            return cursor.fetchone()

    def get_user_email(self, cursor, email):
        return cursor.execute(SELECT_USER_EMAIL, (email,)).fetchone()

    def get_user_salt(self, cursor, email):
        return cursor.execute(SELECT_SALT_USER, (email, )).fetchone()[0]
