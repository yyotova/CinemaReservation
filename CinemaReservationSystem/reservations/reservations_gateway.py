from .models import ReservationModel
from CinemaReservationSystem.database.db import Database


class ReservationGateway:
    def __init__(self):
        # self.model = ReservationModel()
        self.db = Database()
