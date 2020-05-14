import cinema_reservation_system.users.models
from cinema_reservation_system.users.models import User
from cinema_reservation_system.decorators import atomicmethods


@atomicmethods
class UserGateway:
    def __init__(self):
        self.model = cinema_reservation_system.users.models.User

    def create(self, session, *, email, password, salt):
        try:
            session.add(User(email=email, password=password, salt=salt))
            return email
        except Exception as e:
            return e

    def login(self, session, *, email, password):
        return session.query(User.email).filter(User.email == email).filter(User.password == password).first()

    def user(self, session, *, email):
        return session.query(User.user_id).filter(User.email == email).first()

    def get_salt(self, session, salt):
        salt = session.query(User.salt).filter(User.salt == salt).first()
        if salt:
            return salt

    def get_user_email(self, session, email):
        return session.query(User.email).filter(User.email == email).first()

    def get_user_salt(self, session, email):
        return session.query(User.salt).filter(User.email == email).first()
