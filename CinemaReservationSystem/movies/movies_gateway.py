from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.decorators.atomic import atomic


class MovieGateway:
    def __init__(self):
        self.db = Database()

    @atomic
    def get_all_movies(self, cursor):
        # print(cursor)
        cursor.execute('SELECT * FROM movies ORDER BY rating DESC')
        movies = cursor.fetchall()
        # self.db.connection.commit()
        # self.db.connection.close()

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
            # with self.db.connection:
            cursor.execute(search_query, (condition['movie_id'], '%' + condition['date'] + '%'))

        else:
            search_query = '''
                SELECT *
                  FROM projections
                  WHERE movie_id = (?)
            '''
            # with self.db.connection:
            cursor.execute(search_query, (condition['movie_id'], ))

        projections = cursor.fetchall()
        # self.db.connection.commit()
        # self.db.connection.close()

        return projections

    def get_movie_title(self, cursor, *, movie_id):
        # with self.db.connection:
        cursor.execute('SELECT * FROM movies WHERE id = (?)', (movie_id, ))
        title = cursor.fetchone()[1]

        return title
