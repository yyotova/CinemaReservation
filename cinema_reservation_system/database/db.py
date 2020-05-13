from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)


#     def insert_data(self):
#         insert_movie(cursor=self.cursor, name='The Hunger Games: Catching Fire', rating=7.9)
#         insert_movie(cursor=self.cursor, name='Wreck-It Ralph', rating=7.8)
#         insert_movie(cursor=self.cursor, name='Her', rating=8.9)
#         insert_movie(cursor=self.cursor, name='The Irishman', rating=6.9)
#         insert_movie(cursor=self.cursor, name='Black Widow', rating=8.9)
#         insert_movie(cursor=self.cursor, name='The Witch', rating=5.5)

#         insert_projection(cursor=self.cursor, movie_id=1, type='2D', date='2020-05-06', time='10:30')
#         insert_projection(cursor=self.cursor, movie_id=1, type='3D', date='2020-05-06', time='17:30')
#         insert_projection(cursor=self.cursor, movie_id=1, type='4DX', date='2020-05-07', time='17:30')
#         insert_projection(cursor=self.cursor, movie_id=2, type='3D', date='2020-05-07', time='11:30')
#         insert_projection(cursor=self.cursor, movie_id=2, type='2D', date='2020-05-07', time='12:30')
#         insert_projection(cursor=self.cursor, movie_id=3, type='3D', date='2020-05-06', time='15:45')
#         insert_projection(cursor=self.cursor, movie_id=3, type='2D', date='2020-05-06', time='19:50')
#         insert_projection(cursor=self.cursor, movie_id=4, type='4DX', date='2020-05-09', time='20:30')
#         insert_projection(cursor=self.cursor, movie_id=3, type='2D', date='2020-05-08', time='09:30')
#         insert_projection(cursor=self.cursor, movie_id=4, type='3D', date='2020-05-08', time='12:00')
#         insert_projection(cursor=self.cursor, movie_id=5, type='2D', date='2020-05-09', time='10:00')
#         insert_projection(cursor=self.cursor, movie_id=5, type='3D', date='2020-05-08', time='17:30')
#         insert_projection(cursor=self.cursor, movie_id=5, type='3D', date='2020-05-05', time='17:30')
