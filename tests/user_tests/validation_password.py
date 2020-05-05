import unittest
import sys

sys.path.append('.')


from CinemaReservationSystem.users.models import UserModel


class TestPasswordValidation(unittest.TestCase):
    def test_validation_with_less_characters(self):
        user = UserModel(id=1, username="Gosho", password="pass")
        self.assertFalse(user.validate(user.username, user.password))

    def test_validation_with_8_characters_but_no_capital_and_special(self):
        user = UserModel(id=1, username="Gosho", password="passwords")
        self.assertFalse(user.validate(user.username, user.password))

    def test_validation_with_8_characters_capital_no_special(self):
        user = UserModel(id=1, username="Gosho", password="pasSwords")
        self.assertFalse(user.validate(user.username, user.password))

    def test_validation_with_8_characters_but_no_capital_has_special(self):
        user = UserModel(id=1, username="Gosho", password="passwo$rds")
        self.assertFalse(user.validate(user.username, user.password))

    def test_validation_with_valid_styff(self):
        user = UserModel(id=1, username="Gosho", password="pasS$ords")
        self.assertTrue(user.validate(user.username, user.password))


if __name__ == '__main__':
    unittest.main()
