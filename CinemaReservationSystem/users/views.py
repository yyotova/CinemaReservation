from CinemaReservationSystem.users.controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        username = input('username: ')
        password = input('Password: ')

        self.controller.login_user(username=username, password=password)

    def signup(self):
        username = input('username: ')
        password = input('Password: ')

        self.controller.create_user(username=username, password=password)
