from cinema_reservation_system.database.db import Database
from cinema_reservation_system.decorators import atomicmethods


@atomicmethods
class MovieGateway:
    def __init__(self):
        self.db = Database()

    def get_all_movies(self, cursor):
        cursor.execute('SELECT * FROM movies ORDER BY rating DESC')
        movies = cursor.fetchall()

        return movies

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

    def get_movie_title(self, cursor, *, movie_id):
        cursor.execute('SELECT * FROM movies WHERE id = (?)', (movie_id, ))
        title = cursor.fetchone()[1]

        return title
