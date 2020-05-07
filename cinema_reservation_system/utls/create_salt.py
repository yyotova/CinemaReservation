from random import randint

chars = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
'z', 'x', 'c', 'v', 'b', 'n', 'm',
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '$', '_', '*', '.']


def create_salt():
    salt = ''
    for letter in range(0, 4):
        salt += str(chars[randint(0, len(chars) - 1)])

    return salt


'''
test with mock will show only if it reurns salt with 4 chars (mock randint) meaning randint = 4 salt = gggg
'''
