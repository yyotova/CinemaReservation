import unittest
import sys
sys.path.append('.')

from CinemaReservationSystem.decorators.login_required import login_required
from CinemaReservationSystem.utls.cookies import *
from CinemaReservationSystem.config.config_session import SESSION_NAME


class TestDecoratorLogRequest(unittest.TestCase):
    # def test_log_request_decorator_with_no_user(self):
    #     delete_cookie(SESSION_NAME)

    #     @login_required
    #     def func_for_test(msg):
    #         return msg

    #     self.assertFalse(func_for_test())

    # def test_log_request_decorator_with_loged_user(self):
    #     create_cookie(SESSION_NAME, 'user')

    #     @login_required
    #     def func_for_test(msg):
    #         return msg

    #     msg = func_for_test("asdasd")
    #     self.assertEqual(msg, 'asdasd')
    pass
    # change name of file

if __name__ == '__main__':
    unittest.main()
