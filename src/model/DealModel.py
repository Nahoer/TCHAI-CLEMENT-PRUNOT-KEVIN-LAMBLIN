import datetime


class DealModel:

    def __init__(self, id, debtor, receiver, amount, date=datetime.date.today()):
        self.id = id
        self.debtor = debtor
        self.receiver = receiver
        self.amount = amount
        self.date = date
    def __str__(self):
        return str(self.id)+" "+str(self.debtor)+" "+str(self.receiver)+" "+str(self.amount)+" "+str(self.date)