from .users_gateway import UserGateway
from cinema_reservation_system.utls.cookies import *
from cinema_reservation_system.config.config_session import SESSION_NAME
from cinema_reservation_system.utls.hash_pass import hash_password
from cinema_reservation_system.users.models import User


class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, email, password):
        try:
            if User.validate(email, password):
                password, salt = User.create_pass(password)
            if salt:
                user = self.users_gateway.create(email=email, password=password, salt=salt)
            if user:
                create_cookie(SESSION_NAME, user)
        except Exception as e:
            raise e
        return user

    def login_user(self, email, password):
        try:
            if self.users_gateway.get_user_email(email):
                salt = self.users_gateway.get_user_salt(email)
                if salt:
                    password = hash_password(password, salt[0])
                    if password:
                        user = self.users_gateway.login(email=email, password=password)
            else:
                raise Exception("Email doesnt exist")
            if user:
                create_cookie(SESSION_NAME, user[0])
                return user
            else:
                raise Exception("Wrong password")
        except Exception as e:
            raise e

    def take_user_id(self, *, email):
        return self.users_gateway.user(email=email)
