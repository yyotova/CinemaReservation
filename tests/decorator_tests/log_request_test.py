import unittest
import sys
sys.path.append('.')

from CinemaReservationSystem.decorators.login_required import login_required
from CinemaReservationSystem.database.db import Database


def func_for_test(msg):
    print(msg)


class TestDecoratorLogRequest(unittest.TestCase):
    def test_log_request_decorator_with_loged_user(self):
        db = Database()
        db.cursor.execute(CREATE_SESSION)
        db.cursor.execute(INSERT_SESSION, ('Test',))
        @login_required
        func_for_test('test')
        # self.assertEqual(msg, 'test')


if __name__ == '__main__':
    unttest.main()