from cinema_reservation_system.decorators import atomicmethods
from sqlalchemy import and_
from .models import Movie, Projection


@atomicmethods
class MovieGateway:
    def get_all_movies(self, session):
        movies = session.query(Movie.movie_id, Movie.name, Movie.rating).all()

        return movies

    def get_movie_projection(self, session, **condition):
        if 'date' in condition:
            projections = session.query(Projection.projection_id, Projection.movie_id, Projection.movie_type, Projection.date, Projection.time).\
                filter(and_(Projection.movie_id == condition['movie_id'],
                            Projection.date.like(f'%{condition["date"]}%'))).all()

        else:
            projections = session.query(Projection.projection_id, Projection.movie_id, Projection.movie_type, Projection.date, Projection.time).\
                filter(Projection.movie_id == condition['movie_id']).all()

        return projections

    def get_movie_title(self, session, *, movie_id):
        title = session.query(Movie.name).filter(Movie.movie_id == movie_id).first()[0]

        return title
