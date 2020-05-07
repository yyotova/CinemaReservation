from .views import ReservationView
from pandas import *


def print_spots():
    view = ReservationView()
    not_available_spots = view.show_not_available_spots()
    matrix = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            if (i, j) in not_available_spots:
                row.append('X')
            else:
                row.append('.')
        matrix.append(row)

    print(DataFrame(matrix, index=range(1, 11), columns=range(1, 11)))
