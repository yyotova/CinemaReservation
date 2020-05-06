from .movies_gateway import MovieGateway


class MovieController:
    def __init__(self):
        self.movies_gateway = MovieGateway()

    def all_movies(self):
        return self.movies_gateway.get_all_movies()

    def movie_projection(self, *, movie_id, date=None):
        if date is None:
            return self.movies_gateway.get_movie_projection(movie_id=movie_id)
        else:
            return self.movies_gateway.get_movie_projection(movie_id=movie_id, date=date)

    def movie_title(self, *, movie_id):
        return self.movies_gateway.get_movie_title(movie_id=movie_id)
