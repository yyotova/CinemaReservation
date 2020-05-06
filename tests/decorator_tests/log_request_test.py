import unittest
from unittest.mock import patch
import sys
sys.path.append('.')

from CinemaReservationSystem.decorators.login_required import login_required
from CinemaReservationSystem.utls.cookies import *

class TestDecoratorLogRequest(unittest.TestCase):

    @patch('CinemaReservationSystem.decorators.login_required.os', autospec=True)
    def test_log_request_decorator_with_no_user(self, os_mock):
        os_mock.path.exists.return_value = False

        with self.assertRaises(Exception, msg="no user"):
            @login_required
            def func_for_test(msg):
                return msg

    @patch('CinemaReservationSystem.decorators.login_required.os', autospec=True)
    def test_log_request_decorator_with_loged_user(self, os_mock):
        os_mock.path.exists.return_value = True

        @login_required
        def func_for_test(msg):
            return msg

        msg = func_for_test("asdasd")
        self.assertEqual(msg, 'asdasd')


if __name__ == '__main__':
    unittest.main()
