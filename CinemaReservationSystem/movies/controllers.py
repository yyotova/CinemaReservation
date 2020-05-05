from .movies_gateway import MovieGateway


class MovieController:
    def __init__(self):
        self.movies_gateway = MovieGateway()

    def all_movies(self):
        return self.movies_gateway.get_all_movies()
