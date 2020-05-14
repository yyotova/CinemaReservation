from cinema_reservation_system.decorators import atomicmethods
from sqlalchemy import func
from sqlalchemy import and_
from .models import Movie, Projection


@atomicmethods
class MovieGateway:
    def get_all_movies(self, session):
        movies = session.query(Movie).all()

        return movies

    def get_movie_projection(self, session, **condition):
        if 'date' in condition:
            projections = session.query(Projection).\
                filter(and_(Projection.movie_id == condition['movie_id'],
                            Projection.date == condition['date'])).all()

        else:
            projections = session.query(Projection).\
            filter(Projection.movie_id == condition['movie_id']).all()

        return projections

    def get_movie_title(self, session, *, movie_id):
        title = session.query(Movie).filter(Movie.movie_id == movie_id).one()[1]

        return title
