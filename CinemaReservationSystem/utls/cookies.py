import os


def create_cookie(file, info):
    file = open(file, 'w')
    file.write(info)
    file.close()


def read_cookie(file):
    file = open(file, 'r')
    content = file.read()
    file.close()
    return content


def delete_cookie(file):
    if os.path.exists(file):
        os.remove(file)
