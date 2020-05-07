import os
import datetime


def create_cookie(file, info):
    file = open(file, 'w')
    date = datetime.datetime.now()
    file.write(f'{info},{date.year}-{date.month}-{date.day}')
    file.close()


def read_cookie(file):
    file = open(file, 'r')
    content = file.read()
    file.close()
    return content


def delete_cookie(file):
    if session_exists(file):
        os.remove(file)


def session_exists(file):
    return os.path.exists(file)


def delete_cookie_after_date(file):
    if session_exists(file):
        date = datetime.datetime.now() + datetime.timedelta(days=2)
        if read_cookie(file).split(",")[1] == f'{date.year}-{date.month}-{date.day}':
            delete_cookie(file)
