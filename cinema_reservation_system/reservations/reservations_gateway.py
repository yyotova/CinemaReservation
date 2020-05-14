from cinema_reservation_system.decorators import atomicmethods
from sqlalchemy import func
from .models import Reservation
from cinema_reservation_system.movies.models import Movie
from cinema_reservation_system.movies.models import Projection
from cinema_reservation_system.users.models import User


@atomicmethods
class ReservationGateway:
    def available_spots(self, session, *, pr_id):
        count = session.query(func.count(Reservation.reservation_id)).filter(Reservation.projection_id == pr_id).first()

        return 100 - count[0]

    def get_not_available_spots(self, session, *, pr_id):
        return session.query(Reservation.row, Reservation.col).filter(Reservation.projection_id == pr_id).all()

    def make_reservation(self, session, *, user_id, projection_id, seat):
        row = seat[0]
        col = seat[1]
        session.add(Reservation(user_id=user_id[0], projection_id=projection_id, row=row, col=col))

    def info_pr(self, session, *, pr_id):
        return session.query(Projection.date, Projection.time, Projection.movie_type).\
            filter(Projection.projection_id == pr_id).first()

    def get_reservations_of_user(self, session, *, email):
        return session.query(Reservation.reservation_id, Movie.name, Projection.date, Projection.time).\
            join(Projection, Projection.projection_id == Reservation.projection_id).\
            join(Movie, Movie.movie_id == Projection.movie_id).\
            join(User, User.user_id == Reservation.user_id).\
            filter(User.email == email).all()

    def delete_reservation_of_user(self, session, *, proj_id):
        reservation = session.query(Reservation).filter(Reservation.projection_id == proj_id).first()
        session.delete(reservation)
