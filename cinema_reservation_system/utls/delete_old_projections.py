import cinema_reservation_system.movies.models
from cinema_reservation_system.database.db import Session


def delete_passed_projection(*, date):
    Projection = cinema_reservation_system.movies.models.Projection
    print(Session().query(Projection).filter(Projection.date < date).delete())
    Session().commit()
