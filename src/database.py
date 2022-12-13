import datetime
import sqlite3
from typing import List
import hashlib
from model.PersonModel import PersonModel
from model.DealModel import DealModel


class DataBase:
    def __init__(self, path):
        try:
            self.connection = sqlite3.Connection(path)
        except sqlite3.Error as error:
            print("Failed to connect to data base", error)

    def getPerson(self, id:int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Personne WHERE id=?", [id])
        rows = cursor.fetchall()
        if len(rows) != 0:
            for row in rows:
                person = PersonModel(row[0], row[1], row[2], row[3])
            return person
        else:return False

    def getDeal(self, id:int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions where id=?", [id])
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2], row[5])]
        return dealList
        
    def fonctionHachage(string:bytes):
        return hashlib.sha224(string)
    def addPerson(self, last_name, first_name):
        try:
            cursor = self.connection.cursor()
            sqlite_insert_query = """INSERT INTO Personne
                                              (last_name, first_name, public_key) 
                                               VALUES
                                              (?,?,?)"""
            cursor.execute(sqlite_insert_query, [last_name, first_name, public_key] )
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
            personList += [PersonModel(row[0], row[1], row[2], row[3])]
        return personList

    def addTransaction(self, id_envoyeur: int, id_receveur: int, montant: float, date:datetime, hash:str):
        try:
            cursor = self.connection.cursor()
            date = datetime.date.today()
            totalstr = str(id_envoyeur)+str(id_receveur)+str(montant)+str(date)
            dealList = self.getDealList()
            if len(dealList)!=0:
                totalstr += dealList[len(dealList)-1].h
            h = DataBase.fonctionHachage(totalstr.encode("utf-8")).hexdigest()
            sqlite_insert_query = """INSERT INTO Transactions
                                              (id_envoyeur, id_receveur, montant, date, hash) 
                                               VALUES
                                              ('{idEnvoyeur}','{idReceveur}','{montant}', '{date}', '{h}')
                                              """.format(
                                                         idEnvoyeur=id_envoyeur,
                                                         idReceveur=id_receveur,
                                                         montant=montant,
                                                         date=date,
                                                         h=h
                                                         )
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
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2], row[5])]
        return dealList

    def getDealListFromDate(self) -> List[DealModel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions ORDER BY date ASC")
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2], row[5])]
        return dealList

    def getDealForUser(self, id: int) -> List[DealModel]:
        cursor = self.connection.cursor()
        query = """SELECT * FROM Transactions WHERE ? = id_envoyeur OR ? = id_receveur ORDER BY date ASC"""
        cursor.execute(query, [id, id])
        rows = cursor.fetchall()
        dealList = []
        for row in rows:
            dealList += [DealModel(row[0], row[3], row[4], row[1], row[2], row[5])]
        return dealList
