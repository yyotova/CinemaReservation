from .models import ReservationModel
from cinema_reservation_system.database.db import Database
from cinema_reservation_system.decorators import atomic


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    @atomic
    def available_spots(self, cursor, *, pr_id):
        cursor.execute('''SELECT COUNT(projection_id)
            FROM reservations
            WHERE projection_id = (?)
            ''', (pr_id, ))

        return 100 - cursor.fetchone()[0]

    @atomic
    def get_not_available_spots(self, cursor, *, pr_id):
        cursor.execute('''
            SELECT row, col
              FROM reservations
              wHERE projection_id = (?)
            ''', (pr_id, ))
        return cursor.fetchall()

    @atomic
    def make_reservation(self, cursor, *, user_id, projection_id, seat):
        row = seat[0]
        col = seat[1]
        cursor.execute('''
            INSERT INTO reservations(user_id, projection_id, row, col)
              VALUES(?, ?, ?, ?)
            ''', (user_id, projection_id, row, col))

    @atomic
    def info_pr(self, cursor, *, pr_id):
        cursor.execute('''
            SELECT date, time, type
              FROM projections
              WHERE id = (?)
            ''', (pr_id, ))

        return cursor.fetchone()

    @atomic
    def get_reservations_of_user(self, cursor, *, email):
        cursor.execute('''
        SELECT reservations.id,movies.name,projections.date,projections.time,row,col
          FROM reservations
          JOIN projections
          ON reservations.projection_id = projections.id
          JOIN movies
          ON projections.movie_id = movies.id
          JOIN users
          ON reservations.user_id = users.id
          WHERE email= ? ;
        ''', (email, ))
        return cursor.fetchall()

    @atomic
    def delete_reservation_of_user(self, cursor, *, id):
        cursor.execute('''DELETE FROM reservations WHERE id = ? ;''', (id, ))
