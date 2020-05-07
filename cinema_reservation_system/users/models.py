import sys
sys.path.append('.')

from cinema_reservation_system.utls.special_sym_validation import check_for_special_symbol


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        pass_len = len(password) >= 8
        capital_letter = special_symbol = False
        for letter in password:
            if letter.isupper():
                capital_letter = True
            if check_for_special_symbol(letter):
                special_symbol = True

        email_valid = email.count('@') == 1 and email.count('.') >= 1
        pass_valid = pass_len and capital_letter and special_symbol

        if pass_valid and email_valid:
            return True
        else:
            return False
