from cinema_reservation_system.movies.models import Projection
from cinema_reservation_system.database.db import Session


def delete_passed_projection(*, date):
    session = Session()
    projections = session.query(Projection).filter(Projection.date < date).all()
    for projection in projections:
        session.delete(projection)
    session.commit()
