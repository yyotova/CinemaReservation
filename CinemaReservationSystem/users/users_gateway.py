from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.users.models import UserModel
from CinemaReservationSystem.database.user_specific.user_manipulation import *
from CinemaReservationSystem.database.create_tables import *
from CinemaReservationSystem.utls.hash_pass import hash_password
from CinemaReservationSystem.utls.create_salt import create_salt
from CinemaReservationSystem.utls.cookies import *
from CinemaReservationSystem.config.config_session import SESSION_NAME


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, email, password):
        if self.model.validate(email, password):

            salt = create_salt()
            if self.db.cursor.execute(SELECT_SALT, (salt, )):
                salt = create_salt()
            password = hash_password(password, salt)

            self.db.cursor.execute(INSERT_USER, (email, password, salt))  # TODO: create user query
            create_cookie(SESSION_NAME, email)
            self.db.connection.commit()
            self.db.connection.close()
            print(f'Welcome user :{read_cookie(SESSION_NAME).split(",")[0]}')
            return True
        # TODO: What whould I return?
        else:
            # add better text later
            print("Wrong password and email")
        return False

    def login(self, *, email, password):
        # fix if no salt
        if self.db.cursor.execute(SELECT_USER_EMAIL, (email,)).fetchone():
            salt = self.db.cursor.execute(SELECT_SALT_USER, (email, )).fetchone()[0]

            if salt:
                password = hash_password(password, salt)
            else:
                return False

            if self.db.cursor.execute(SELECT_USER, (email, password)).fetchone():
                create_cookie(SESSION_NAME, email)
                print(f'Welcome user :{read_cookie(SESSION_NAME).split(",")[0]}')
                return True
            else:
                print('Wrong password')
        else:
            print("Wrong username")
        return False

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]
