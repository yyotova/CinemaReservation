class UserModel:
    def __init__(self, *, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def validate(username, password):
        # TODO: Implement a validation -> Raise an error
        pass_len = len(password) > 8
        capital_letter = False
        special_symbol = not password.isidentifier()
        for letter in password:
            if letter.isupper():
                capital_letter = True
        if pass_len and capital_letter and special_symbol:
            return True
        else:
            return False
