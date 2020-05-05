import unittest
import sys
sys.path.append('.')

from CinemaReservationSystem.decorators.login_required import login_required
from CinemaReservationSystem.database.db import Database
from CinemaReservationSystem.database.create_tables import *
from CinemaReservationSystem.database.session_specific.session_manipulation import *

class TestDecoratorLogRequest(unittest.TestCase):
    def test_log_request_decorator_with_loged_user(self):
        db = Database()
        db.cursor.execute(CREATE_SESSION)
        db.cursor.execute(INSERT_SESSION, ('Test',))
        print(db.cursor.execute(SELECT_SESSION).fetchone()[0])
        @login_required
        def func_for_test(msg):
            return msg
        msg = func_for_test('test')
        self.assertEqual(msg, 'test')


if __name__ == '__main__':
    unittest.main()