from CinemaReservationSystem.users.controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        email= input('email: ')
        password = input('Password: ')

        self.controller.login_user(email=email, password=password)

    def signup(self):
        email = input('email: ')
        password = input('Password: ')

        self.controller.create_user(email=email, password=password)
