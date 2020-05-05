from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.users.models import UserModel
from CinemaReservationSystem.database.session_specific.create_session import INSERT_SESSION
from CinemaReservationSystem.database.user_specific.create_new_user import INSERT_USER
from CinemaReservationSystem.utls.hash_pass import hash_password
from CinemaReservationSystem.utls.create_salt import create_salt
from CinemaReservationSystem.database.user_specific.check_for_salt import SELECT_SALT
from CinemaReservationSystem.database.user_specific.select_user import SELECT_USER
from CinemaReservationSystem.database.create_tables import CREATE_SESSION
from CinemaReservationSystem.database.session_specific.select_session import SELECT_SESSION


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, email, password):
        if self.model.validate(email, password) is True:

            salt = create_salt()
            if self.db.cursor.execute(SELECT_SALT, ('salt', salt)):
                salt = create_salt()
            password = hash_password(password, salt)

            self.db.cursor.execute(INSERT_USER, (email, password, salt))  # TODO: create user query
            self.db.cursor.execute(CREATE_SESSION)
            # self.db.connection.connection()
            self.db.cursor.execute(INSERT_SESSION, (email,))
            print(self.db.cursor.execute(SELECT_SESSION))
            self.db.connection.commit()
            self.db.connection.close()
        # TODO: What whould I return?
        else:
            print("ops")

    def login(self, *, email, password):
        salt = self.db.cursor.execute(SELECT_SALT, ('email', email)).fetchone()[0]
        
        password = hash_password(password, salt)
        # print(self.db.cursor.execute(SELECT_USER, (email, password)).fetchone())
        if self.db.cursor.execute(SELECT_USER, (email, password)).fetchone():
            print('inseide')
            self.db.cursor.execute(CREATE_SESSION)
            self.db.cursor.execute(INSERT_SESSION, (email,))
            print(self.db.cursor.execute(SELECT_SESSION).fetchone())
            self.db.connection.commit()
            self.db.connection.close()

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]
