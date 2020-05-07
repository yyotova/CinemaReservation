import sys
sys.path.append('.')
from cinema_reservation_system.users.controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        email = input('email: ')
        password = input('Password: ')

        return self.controller.login_user(email=email, password=password)

    def signup(self):
        constraint = f'''
        Passwords should be with length at least 8 symbols,
        1 capital letter and a special symbol.
        '''
        email = input('email: ')
        print(constraint)
        password = input('Password: ')

        return self.controller.create_user(email=email, password=password)

    def user_id(self, *, email):
        return self.controller.take_user_id(email=email)
