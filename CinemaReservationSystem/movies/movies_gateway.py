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
