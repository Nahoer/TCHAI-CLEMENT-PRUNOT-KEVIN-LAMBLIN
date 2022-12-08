import datetime
import sqlite3
from typing import List
from model.PersonModel import PersonModel
from model.DealModel import DealModel


class DataBase:
    def __init__(self, path):
        try:
            self.connection = sqlite3.Connection(path)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def getPerson(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Personne WHERE id={id}".format(id=id))
        rows = cursor.fetchall()
        personList = []
        for row in rows:
            personList += [PersonModel(row[0], row[2], row[1])]
        return personList

    def getDeal(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions where id={id}".format(id=id))
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2])]
        return dealList

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

    def getPersonList(self) -> List[PersonModel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Personne")
        rows = cursor.fetchall()
        personList = []
        for row in rows:
            personList += [PersonModel(row[0], row[2], row[1])]
        return personList

    def addTransaction(self, id_envoyeur: int, id_receveur: int, montant: int):
        try:
            cursor = self.connection.cursor()
            sqlite_insert_query = """INSERT INTO Transactions
                                              (id_envoyeur, id_receveur, montant, date) 
                                               VALUES
                                              ('{}','{}','{}', '{}')""".format(id_envoyeur, id_receveur, montant,
                                                                               datetime.date.today())
            count = cursor.execute(sqlite_insert_query)
            self.connection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()
        except sqlite3.Error as error:
            print("Erreur lors de l'insertion de la transaction: ", error)

    def getDealList(self) -> List[DealModel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions")
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2])]
        return dealList

    def getDealListFromDate(self) -> List[DealModel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions ORDER BY date ASC")
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2])]
        return dealList

    def getDealForUser(self, id: int) -> List[DealModel]:
        cursor = self.connection.cursor()
        query = """SELECT * FROM Transactions WHERE '{}' = id_envoyeur OR '{}' = id_receveur ORDER BY date ASC""".format(
            id,
            id)
        cursor.execute(query)
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2])]
        return dealList
