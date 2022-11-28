import datetime

from PersonModel import PersonModel


class DealModel:
    id = 0
    debtor = PersonModel()
    receiver = PersonModel()
    amount = 0
    date = datetime.datetime()

    def __init__(self, id, debtor, receiver, amount, date=datetime.date.today()):
        self.id = id
        self.debtor = debtor
        self.receiver = receiver
        self.amount = amount
        self.date = date
