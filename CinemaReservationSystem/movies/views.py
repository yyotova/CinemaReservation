from .controllers import MovieController
from tabulate import tabulate


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def print_all_movies(self):
        all_movies = self.controller.all_movies()
        print(tabulate([movie for movie in all_movies], headers=['id', 'name', 'rating'], tablefmt='pretty'))

    def print_movie_projections(self, *, movie_id, date=None):
        projections = self.controller.movie_projection(movie_id=movie_id, date=date)
        print(tabulate([info for info in projections], headers=['id', 'movie_id', 'type', 'date', 'time'], tablefmt='pretty'))
