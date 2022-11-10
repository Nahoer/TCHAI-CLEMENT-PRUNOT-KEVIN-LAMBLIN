import sqlite3
from typing import List
from model.PersonModel import PersonModel as Person
from model.DealModel import DealModel as Deal
class DataBase:
    def __init__(self, path):
        try:
            self.connection = sqlite3.Connection(path)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
    def addPerson(self, last_name, first_name):
        try:
            cursor = self.connection.cursor()
            sqlite_insert_query = """INSERT INTO Personne
                                              (last_name, first_name) 
                                               VALUES
                                              ('{}','{}')""".format(last_name, first_name)
            count = cursor.execute(sqlite_insert_query)
            self.connection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()
        except sqlite3.Error as error:
            print("Erreur lors de l'insertion de la personne: ", error)
    def getPersonList(self)->List[Person]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Personne")
        rows = cursor.fetchall()
        personList = []
        for row in rows:
            personList += [Person(row[1], row[2], row[0])]
        return personList

    def addTransaction(self, id_envoyeur, id_receveur, montant, date):
        try:
            cursor = self.connection.cursor()
            sqlite_insert_query = """INSERT INTO Transactions
                                              (id_envoyeur, id_receveur, montant, date) 
                                               VALUES
                                              ('{}','{}')""".format(id_envoyeur, id_receveur, montant, date)
            count = cursor.execute(sqlite_insert_query)
            self.connection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()
        except sqlite3.Error as error:
            print("Erreur lors de l'insertion de la transaction: ", error)

    def getDealList(self)->List[Deal]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions")
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [Person(row[1], row[2], row[0])]
        return dealList