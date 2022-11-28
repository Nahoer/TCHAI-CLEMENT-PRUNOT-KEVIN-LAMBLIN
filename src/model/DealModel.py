import datetime


class DealModel:

    def __init__(self, id, debtor, receiver, amount, date=datetime.date.today()):
        self.id = id
        self.debtor = debtor
        self.receiver = receiver
        self.amount = amount
        self.date = date
