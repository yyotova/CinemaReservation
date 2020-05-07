from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.decorators import atomic


class MovieGateway:
    def __init__(self):
        self.db = Database()

    @atomic
    def get_all_movies(self, cursor):
        cursor.execute('SELECT * FROM movies ORDER BY rating DESC')
        movies = cursor.fetchall()

        return movies

    @atomic
    def get_movie_projection(self, cursor, **condition):
        if 'date' in condition:
            search_query = '''
                SELECT *
                  FROM projections
                  WHERE movie_id = (?)
                    AND date LIKE (?)
            '''
            cursor.execute(search_query, (condition['movie_id'], '%' + condition['date'] + '%'))

        else:
            search_query = '''
                SELECT *
                  FROM projections
                  WHERE movie_id = (?)
            '''
            cursor.execute(search_query, (condition['movie_id'], ))

        projections = cursor.fetchall()

        return projections

    @atomic
    def get_movie_title(self, cursor, *, movie_id):
        cursor.execute('SELECT * FROM movies WHERE id = (?)', (movie_id, ))
        title = cursor.fetchone()[1]

        return title
