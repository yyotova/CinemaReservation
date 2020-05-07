from .controllers import ReservationController
from CinemaReservationSystem.movies.views import MovieView
from tabulate import tabulate


class ReservationView:
    def __init__(self):
        self.controler = ReservationController()

    def make_reservation(self):
        self.tickets = input('Choose number of tickets: ')
        movie_view = MovieView()
        movie_view.print_all_movies()

        choosen_movie = input('Choose a movie: ')
        title = movie_view.print_movie_title(movie_id=choosen_movie)
        print(f'Projections for movie "{title}": ')
        projections = self.controler.get_available_spots(movie_id=choosen_movie)

        headers = ['id', 'movie_id', 'type', 'date', 'time', 'available_spots']
        print(tabulate([info for info in projections], headers=headers, tablefmt='pretty'))

    def show_not_available_spots(self):
        choosen_projection = input('Choose a projection: ')
        return self.controler.not_available_spots(pr_id=choosen_projection)
