import hashlib


def hash_password(password, salt):
    return hashlib.sha512((password + salt).encode()).hexdigest()


'''
mocking hash will make it useless maybe
'''
