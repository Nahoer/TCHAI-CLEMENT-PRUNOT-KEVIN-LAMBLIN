import sqlite3

class DataBase:
    def __init__(self, path):
        self.connection = sqlite3.Connection(path)
        