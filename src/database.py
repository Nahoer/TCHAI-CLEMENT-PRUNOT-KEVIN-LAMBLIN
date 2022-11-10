import sqlite3
import Person
class DataBase:
    def __init__(self, path):
        try:
            self.connection = sqlite3.Connection(path)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
    def addPerson(self, personne:Person):
        cursor = self.connection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = """INSERT INTO SqliteDb_developers
                                          (id, name, email, joining_date, salary) 
                                           VALUES 
                                          (1,'James','james@pynative.com','2019-03-17',8000)"""
        count = cursor.execute(sqlite_insert_query)
        self.connection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()