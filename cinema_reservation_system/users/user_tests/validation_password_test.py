import unittest
from cinema_reservation_system.users.models import User


class TestPasswordValidation(unittest.TestCase):
    def test_validation_with_less_characters(self):
        user = User(email="ppp@abv.bg", password="pass")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)

    def test_validation_with_8_characters_but_no_capital_and_special(self):
        user = User(email="ppp@abv.bg", password="passwords")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)

    def test_validation_with_8_characters_capital_no_special(self):
        user = User(email="ppp@abv.bg", password="pasSwords")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)

    def test_validation_with_8_characters_but_no_capital_has_special(self):
        user = User(email="ppp@abv.bg", password="passwo$rds")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)

    def test_validation_with_worng_mail_no_nokey_a(self):
        user = User(email="pppabv.bg", password="Passwo$rds")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)

    def test_validation_with_wrong_mail_no_dotself(self):
        user = User(email="ppp@abvbg", password="PasS$ords")
        with self.assertRaises(Exception):
            user.validate(user.email, user.password)


if __name__ == '__main__':
    unittest.main()
