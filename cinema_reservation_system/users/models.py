# from cinema_reservation_system.utls.special_sym_validation import check_for_special_symbol
# from cinema_reservation_system.utls.create_salt import create_salt
# from cinema_reservation_system.utls.hash_pass import hash_password
# import cinema_reservation_system.users.users_gateway
from cinema_reservation_system.database.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)

    def __repr__(self):
        return f'{self.email}'


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        pass_len = len(password) >= 8
        capital_letter = special_symbol = False
        for letter in password:
            if letter.isupper():
                capital_letter = True
            if check_for_special_symbol(letter):
                special_symbol = True

        email_valid = email.count('@') == 1 and email.count('.') >= 1
        pass_valid = pass_len and capital_letter and special_symbol

        if pass_valid and email_valid:
            return True
        else:
            raise Exception("Wrong username or password")

    @staticmethod
    def create_pass(password):
        salt = create_salt()
        if cinema_reservation_system.users.users_gateway.UserGateway().get_salt(salt) is None:
            salt = create_salt()
        password = hash_password(password, salt)
        return password, salt
