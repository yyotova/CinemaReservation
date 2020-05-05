from .controllers import MovieController
from tabulate import tabulate


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def print_all_movies(self):
        all_movies = self.controller.all_movies()
        print(tabulate([movie for movie in all_movies], headers=['id', 'name', 'rating']))
