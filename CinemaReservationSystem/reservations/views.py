from .controllers import ReservationController
from CinemaReservationSystem.movies.views import MovieView
from CinemaReservationSystem.users import UserViews
from CinemaReservationSystem.decorators import login_required
from tabulate import tabulate
from pandas import *


class ReservationView:

    @login_required
    def __init__(self):
        self.controler = ReservationController()
        self.user = UserViews()

    def make_reservation(self):
        self.tickets = int(input('Choose number of tickets: '))
        movie_view = MovieView()
        movie_view.print_all_movies()

        self.choosen_movie = input('Choose a movie: ')
        title = movie_view.print_movie_title(movie_id=self.choosen_movie)
        print(f'Projections for movie "{title}": ')
        projections = self.controler.get_available_spots(movie_id=self.choosen_movie)

        headers = ['id', 'movie_id', 'type', 'date', 'time', 'available_spots']
        print(tabulate([info for info in projections], headers=headers, tablefmt='pretty'))
        self.choosen_projection = input('Choose a projection: ')

    def print_spots(self):
        self.not_available_spots = self.controler.not_available_spots(pr_id=self.choosen_projection)
        matrix = []
        for i in range(1, 11):
            row = []
            for j in range(1, 11):
                if (i, j) in self.not_available_spots:
                    row.append('X')
                else:
                    row.append('.')
            matrix.append(row)

        print(DataFrame(matrix, index=range(1, 11), columns=range(1, 11)))

    def choose_seat(self, *, email):
        user_id = self.user.user_id(email=email)
        for i in range(1, self.tickets + 1):
            exit = False
            while not exit:
                choosen_seat = input(f'Choose seat {i}: ')
                choosen_seat = choosen_seat.replace('(', '').replace(')', '')
                choosen_seat = choosen_seat.split(',')
                choosen_seat = [int(x) for x in choosen_seat]
                if tuple(choosen_seat) in self.not_available_spots:
                    print('This seat is already taken!')
                elif choosen_seat[0] < 0 or choosen_seat[1] > 10:
                    print('Lol...NO!')
                else:
                    self.controler.take_seat(user_id=user_id, projection_id=self.choosen_projection, seat=choosen_seat)
                    exit = True
