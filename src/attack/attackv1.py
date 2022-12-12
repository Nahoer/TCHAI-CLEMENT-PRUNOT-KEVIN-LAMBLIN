import sqlite3
import requests

base_url = "http://127.0.0.1:5000"
path = "../../database/test.db"


class DataBase:
    def __init__(self, path):
        try:
            self.connection = sqlite3.Connection(path)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def update(self):
        # Update a deal with setting the amount to 0
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Transactions SET montant = '0' where id = 3")
        self.connection.commit()



db = DataBase(path)

# Show the list of deals ordered by date
print("Liste des transactions par date avec la modification: ")
r = requests.get(base_url + "/transactions")
print(r.text)
print()

# Update database value
db.update()

# Show again the list of deals ordered by date
print("Liste des transactions par date : ")
r = requests.get(base_url + "/transactions")
print(r.text)
print()
