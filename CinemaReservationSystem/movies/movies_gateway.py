from CinemaReservationSystem.database.db import Database


class MovieGateway:
    def __init__(self):
        self.db = Database()

    def get_all_movies(self):
        self.db.cursor.execute('SELECT * FROM movies ORDER BY rating DESC')
        movies = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()

        return movies

    def get_movie_projection(self, **condition):
        if 'date' in condition:
            search_query = '''
                SELECT *
                  FROM projections
                  WHERE movie_id = (?)
                    AND date LIKE (?)
            '''
            self.db.cursor.execute(search_query, (condition['movie_id'], '%' + condition['date'] + '%'))

        else:
            search_query = '''
                SELECT *
                  FROM projections
                  WHERE movie_id = (?)
            '''
            self.db.cursor.execute(search_query, (condition['movie_id'], ))

        projections = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()

        return projections
