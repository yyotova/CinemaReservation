from .reservations_gateway import ReservationGateway


class ReservationController:
    def __init__(self):
        self.reservation_gateway = ReservationGateway()


