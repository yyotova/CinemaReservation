from CinemaReservationSystem.utls.special_sym_validation import check_for_special_symbol


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        # TODO: Implement a validation -> Raise an error
        pass_len = len(password) >= 8

        capital_letter = special_symbol = False
        for letter in password:
            if letter.isupper():
                capital_letter = True
            if check_for_special_symbol(letter):
                special_symbol = True

        if pass_len and capital_letter and special_symbol:
            return True
        else:
            return False
