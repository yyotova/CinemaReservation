import unittest
from cinema_reservation_system.utls.special_sym_validation import check_for_special_symbol


class TestSpecialSym_validation(unittest.TestCase):

    def test_secial_sym_validation_with_special_sym(self):
        self.assertTrue(check_for_special_symbol('_'))

    def test_secial_sym_validation_with_letter(self):
        self.assertFalse(check_for_special_symbol('a'))

    def test_secial_sym_validation_with_capital_letter(self):
        self.assertFalse(check_for_special_symbol('A'))

    def test_secial_sym_validation_with_numer(self):
        self.assertFalse(check_for_special_symbol('1'))


if __name__ == '__main__':
    unittest.main()
