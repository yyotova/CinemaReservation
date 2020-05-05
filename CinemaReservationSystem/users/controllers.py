from CinemaReservationSystem.users.users_gateway import UserGateway


class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, username, password):
        user = self.users_gateway.create(username=username, password=password)

        # send email
        # sync with Slack

        return user

    def login_user(self, username, password):
        user = self.users_gateway.login(username=username, password=password)
        return user