import unittest
import sys
sys.path.append('.')

from cinema_reservation_system.users.controllers import UserContoller  # noqa


class TestUsersController(unittest.TestCase):
    def test_contoller_create(self):
        controller = UserContoller()
        email = 'worng'
        password = 'worng'
        with self.assertRaises(Exception, msg='Worng usersname or password'):
            controller.create_user(email=email, password=password)

    def test_contoller_login_wrong_email(self):
        controller = UserContoller()
        email = 'worng'
        password = 'worng'
        with self.assertRaises(Exception, msg='Email doesnt exist'):
            controller.login_user(email=email, password=password)

    def test_contoller_login_worng_password(self):
        controller = UserContoller()
        email = 'petar@abv.bg'
        password = 'worng'
        with self.assertRaises(Exception, msg='Worng password'):
            controller.login_user(email=email, password=password)


if __name__ == '__main__':
    unittest.main()
