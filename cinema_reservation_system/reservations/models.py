from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from cinema_reservation_system.database.db import Base
from cinema_reservation_system.users.models import User
from cinema_reservation_system.movies.models import Projection


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
