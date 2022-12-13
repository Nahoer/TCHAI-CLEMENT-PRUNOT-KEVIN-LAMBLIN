import datetime


class DealModel:

    def __init__(self, id, debtor, receiver, amount, date, h):
        self.id = id
        self.debtor = debtor
        self.receiver = receiver
        self.amount = amount
        self.date = date
        self.h = h

    def __str__(self):
        return str(self.id) + " " + str(self.debtor) + " " + str(self.receiver) + " " + str(self.amount) + " " + str(
            self.date)

    def toJSON(self):
        JSON = {}
        JSON["id"] = self.id
        JSON["idEnvoyeur"] = self.debtor
        JSON["idReceveur"] = self.receiver
        JSON["montant"] = self.amount
        JSON["date"] = self.date
        JSON["hash"] = self.h
        return JSON
