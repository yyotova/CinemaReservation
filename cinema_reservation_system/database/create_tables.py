from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, CheckConstraint, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///cinema.db")
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)

    def __repr__(self):
        return f'{self.email}'


class Movie(Base):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float, CheckConstraint('rating>0 and rating<10'))

    def __repr__(self):
        return f'name: {self.name}  rating: {self.rating}'


class Projection(Base):
    __tablename__ = 'projections'
    projection_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.movie_id))
    movie = relationship(Movie, backref='projections')
    movie_type = Column(String)
    date = Column(String)
    time = Column(String)

    def __repr__(self):
        return f'projection: {self.projection_id}, movie: {self.movie_id},\
            date: {self.date}, time: {self.time}'


class Reservation(Base):
    __tablename__ = 'reservations'
    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    user = relationship(User, backref='reservations')
    projection_id = Column(Integer, ForeignKey(Projection.projection_id))
    projection = relationship(Projection, backref='reservations')
    row = Column(Integer, CheckConstraint('row>0 and row<10'))
    col = Column(Integer, CheckConstraint('col>0 and col<10'))

    def __repr__(self):
        return f'res: {self.reservation_id}, user: {self.user_id},\
            projection: {self.projection_id}, row: {self.row}, col: {self.col}'
