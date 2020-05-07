from ..users import UserGateway


class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, email, password):
        user = self.users_gateway.create(email=email, password=password)

        return user

    def login_user(self, email, password):
        user = self.users_gateway.login(email=email, password=password)
        return user

    def take_user_id(self, *, email):
        return self.users_gateway.user(email=email)
