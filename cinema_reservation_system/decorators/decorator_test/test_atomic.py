
import unittest
import sys
sys.path.append('.')
from cinema_reservation_system.decorators.atomic import atomic
from cinema_reservation_system.movies.models import Movie

class Test(object):
    """docstring for Test"""    
    @atomic
    def add(self, session):
        session.add(Movie(name='test1', rating=3.4))
        # return 1

def main():
    Test().add()

if __name__ == '__main__':
    main()