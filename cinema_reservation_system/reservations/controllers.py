from .reservations_gateway import ReservationGateway
from cinema_reservation_system.movies.views import MovieView


class ReservationController:
    def __init__(self):
        self.reservation_gateway = ReservationGateway()

    def get_available_spots(self, *, movie_id):
        movie_view = MovieView()
        projections = movie_view.get_projections(movie_id=movie_id)

        available_spots = []
        for p in projections:
            available_spots.append(self.reservation_gateway.available_spots(pr_id=p[0]))

        for i in range(0, len(projections)):
            projections[i] = list(projections[i])
            projections[i].append(available_spots[i])

        return projections

    def not_available_spots(self, *, pr_id):
        return self.reservation_gateway.get_not_available_spots(pr_id=pr_id)

    def take_seat(self, *, user_id, projection_id, seat):
        self.reservation_gateway.make_reservation(user_id=user_id, projection_id=projection_id, seat=seat)

    def info(self, *, pr_id):
        return self.reservation_gateway.info_pr(pr_id=pr_id)
