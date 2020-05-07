import sqlite3

from ..config import DB_NAME


def insert_movie(*, cursor, name, rating):
    cursor.execute('INSERT INTO movies (name, rating) VALUES (?, ?)', (name, rating))


def insert_projection(*, cursor, movie_id, type, date, time):
    cursor.execute('INSERT INTO projections (movie_id, type, date, time) VALUES (?, ?, ?, ?)', (movie_id, type, date, time))


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def insert_data(self):
        insert_movie(cursor=self.cursor, name='The Hunger Games: Catching Fire', rating=7.9)
        insert_movie(cursor=self.cursor, name='Wreck-It Ralph', rating=7.8)
        insert_movie(cursor=self.cursor, name='Her', rating=8.9)
        insert_movie(cursor=self.cursor, name='The Irishman', rating=6.9)
        insert_movie(cursor=self.cursor, name='Black Widow', rating=8.9)
        insert_movie(cursor=self.cursor, name='The Witch', rating=5.5)

        insert_projection(cursor=self.cursor, movie_id=1, type='2D', date='2020-05-06', time='10:30')
        insert_projection(cursor=self.cursor, movie_id=1, type='3D', date='2020-05-06', time='17:30')
        insert_projection(cursor=self.cursor, movie_id=1, type='4DX', date='2020-05-07', time='17:30')
        insert_projection(cursor=self.cursor, movie_id=2, type='3D', date='2020-05-07', time='11:30')
        insert_projection(cursor=self.cursor, movie_id=2, type='2D', date='2020-05-07', time='12:30')
        insert_projection(cursor=self.cursor, movie_id=3, type='3D', date='2020-05-06', time='15:45')
        insert_projection(cursor=self.cursor, movie_id=3, type='2D', date='2020-05-06', time='19:50')
        insert_projection(cursor=self.cursor, movie_id=4, type='4DX', date='2020-05-09', time='20:30')
        insert_projection(cursor=self.cursor, movie_id=3, type='2D', date='2020-05-08', time='09:30')
        insert_projection(cursor=self.cursor, movie_id=4, type='3D', date='2020-05-08', time='12:00')
        insert_projection(cursor=self.cursor, movie_id=5, type='2D', date='2020-05-09', time='10:00')
        insert_projection(cursor=self.cursor, movie_id=5, type='3D', date='2020-05-08', time='17:30')
        insert_projection(cursor=self.cursor, movie_id=5, type='3D', date='2020-05-05', time='17:30')

    def delete_passed_projection(self, *, date):
        self.cursor.execute('DELETE FROM projections WHERE date < (?)', (date, ))
