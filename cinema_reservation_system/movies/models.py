from sqlalchemy import Column, Integer, String, CheckConstraint, Float, ForeignKey
from sqlalchemy.orm import relationship
from cinema_reservation_system.database.db import Base


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
