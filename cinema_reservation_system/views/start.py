from cinema_reservation_system.config.config_session import SESSION_NAME
from cinema_reservation_system.reservations import ReservationView
from cinema_reservation_system.movies import MovieView
from cinema_reservation_system.views import welcome, menu, session_menu
from cinema_reservation_system.utls.cookies import *
from cinema_reservation_system.utls.check_session import check_for_session


def start():
    print('Welcome to HackCinema!')
    exit = False
    loged = False
    if check_for_session():
        choise = session_menu()
        if choise == '1':
            exit = False
            loged = True
        if choise == '2':
            delete_cookie(SESSION_NAME)
    if not loged:
        if not welcome():
            exit = True
            loged = True
    while not exit:
        menu()
        command = input('Command: ')
        if command == '1':
            movie_view = MovieView()
            movie_view.print_all_movies()

        elif command == '2':
            movie_view = MovieView()
            movie_id = input('Enter movie_id: ')
            date = input('Enter date(optional): ')
            movie_view.print_movie_projections(movie_id=movie_id, date=date)
        elif command == '3':
            reservation_view = ReservationView()
            if reservation_view:
                reservation_view.step_1()
                cont = input('Do you want to continue? ')
                if cont in ['yes', 'y']:
                    reservation_view.step_2()
                else:
                    break
                cont = input('Do you want to continue? ')
                if cont in ['yes', 'y']:
                    reservation_view.step_3()
                else:
                    break
                cont = input('Do you want to continue? ')
                if cont in ['yes', 'y']:
                    reservation_view.step_4()
                else:
                    break
                cont = input('Do you want to continue? ')
                if cont in ['yes', 'y']:
                    email = read_cookie(SESSION_NAME).split(',')[0]
                    reservation_view.step_5(email=email)
                else:
                    break
            else:
                print('You have to log in to make reservation!')
                welcome()

        elif command == '5':
            exit = True
