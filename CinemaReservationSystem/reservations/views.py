from .controllers import ReservationController
from CinemaReservationSystem.movies.views import MovieView
from CinemaReservationSystem.users import UserViews
from CinemaReservationSystem.decorators import login_required, log_info
from tabulate import tabulate
from pandas import *


@login_required
class ReservationView:
    def __init__(self):
        self.controler = ReservationController()
        self.user = UserViews()
        self.movie_view = MovieView()

    def step_1(self):
        self.tickets = int(input('Choose number of tickets: '))
        print('Current movies: ')
        self.movie_view.print_all_movies()

    def step_2(self):
        self.choosen_movie = input('Choose a movie: ')
        self.title = self.movie_view.print_movie_title(movie_id=self.choosen_movie)
        print(f'Projections for movie "{self.title}": ')
        self.projection = self.controler.get_available_spots(movie_id=self.choosen_movie)

        headers = ['id', 'movie_id', 'type', 'date', 'time', 'available_spots']
        print(tabulate([info for info in self.projection], headers=headers, tablefmt='pretty'))

    def step_3(self):
        self.choosen_projection = input('Choose a projection: ')
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

    def step_4(self):
        for i in range(1, self.tickets + 1):
            exit = False
            while not exit:
                self.choosen_seat = input(f'Choose seat {i}: ')
                self.choosen_seat = self.choosen_seat.replace('(', '').replace(')', '')
                self.choosen_seat = self.choosen_seat.split(',')
                self.choosen_seat = [int(x) for x in self.choosen_seat]
                seats = []
                if tuple(self.choosen_seat) in self.not_available_spots:
                    print('This seat is already taken!')
                elif self.choosen_seat[0] < 0 or self.choosen_seat[1] > 10:
                    print('Lol...NO!')
                else:
                    seats.append(self.choosen_seat)
                    exit = True

        print('This is your reservation: ')
        info = self.controler.info(pr_id=self.choosen_projection)
        print(f'''
            Movie:  {self.title}
            Date and time: {info[0]}, {info[1]} ({info[2]})
            ''')

    @log_info
    def step_5(self, *, email):
        confirm = input('Confirm - type \'finalize\': ')
        if confirm == 'finalize':
            user_id = self.user.user_id(email=email)
            self.controler.take_seat(user_id=user_id, projection_id=self.choosen_projection, seat=self.choosen_seat)
            print('Thanks!')
            return f'email: {email} projection: {self.choosen_projection} seat: {self.choosen_seat}'
