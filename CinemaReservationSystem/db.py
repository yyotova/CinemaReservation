import sqlite3
from settings import DB_NAME


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
