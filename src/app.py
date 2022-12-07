from flask import Flask, request
from database import DataBase

app = Flask(__name__)

# Variable contenant le chemin à la base de données
path = "../database/transactions.db"


def checkParams(requestArgs, list: [str]):
    # Vérifie que tous les paramètres de requête passés en paramètre sont dans la liste d'argument de la requête
    ok = True
    for param in list:
        if not (param in requestArgs):
            ok = False
    return ok


@app.route('/addTransaction')
def addTransaction():
    db = DataBase(path)
    message = "La transaction a bien été enregistrée."
    if checkParams(request.args, ['idSender', 'idReceiver', 'amount']):
        idEnvoyeur = int(request.args.get("idSender"))
        idReceveur = int(request.args.get("idReceiver"))
        montant = float(request.args.get("amount"))
        db.addTransaction(idEnvoyeur, idReceveur, montant)
        return message
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "idEnvoyeur: id de l'auteur de la transaction<br/>"
        message += "idReceveur: personne qui reçoit l'argent de la transaction<br/>"
        message += "montant: montant de la transaction<br/>"
        return message


@app.route('/transactions')
def listerTransactions():
    db = DataBase(path)
    liste = db.getDealList()
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab


@app.route('/addPerson')
def addPersonne():  # /addPerson?firstName=<firstname>&lastName=<lastname> sans quote pour ajouter
    db = DataBase(path)

    message = "La personne a bien été ajoutée."
    if checkParams(request.args, ['lastName', 'firstName']):
        first_name = str(request.args.get("firstName"))
        last_name = str(request.args.get("lastName"))
        db.addPerson(last_name, first_name)
        return message
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "firstName: id de l'auteur de la transaction<br/>"
        message += "lastName: personne qui reçoit l'argent de la transaction"
        return message


@app.route('/persons')
def listerPersonnes():
    db = DataBase(path)
    liste = db.getPersonList()
    tab = []
    for person in liste:
        tab += [person.toJSON()]
    return tab


@app.route('/connexion')
def connexion():
    return "Connexion OK"


@app.route('/transactionsOrderedByDate')
def listerTransactionsParDate():
    db = DataBase(path)
    liste = db.getDealListFromDate()
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab


@app.route('/transactionsFor')
def listerTransactionPour():
    db = DataBase(path)
    id = -1
    if checkParams(request.args, ['id']):
        id = int(request.args.get("id"))

    if id >= 0:
        message = ""
        liste = db.getDealForUser(id)
        tab = []
        for deal in liste:
            tab += [deal.toJSON()]
        return tab
    else:
        return "Id invalide"




@app.route('/getSolde')
def getSolde():
    db = DataBase(path)
    listeDeal = db.getDealList()
    listePersons = db.getPersonList()
    listeID = {}
    if checkParams(request.args, ['idPerson']):
        listeID[int(request.args["idPerson"])] = 0
    else:
        for person in listePersons:
            listeID[person.id] = 0
    for id in listeID:
        for deal in listeDeal:
            if deal.debtor == id:
                listeID[id] -= deal.amount
                print(str(id) + " a payé " + str(deal.amount))
            elif deal.receiver == id:
                listeID[id] += deal.amount
                print(str(id) + " a reçu " + str(deal.amount))
    return listeID

@app.route("/verifyIntegrity")
def verifyIntegrity():
    db = DataBase(path)
    deals = db.getDealList()
    wrong = []
    for deal in deals:
        totalstr = str(deal.debtor)+str(deal.receiver)+str(deal.amount)+str(deal.date)
        if(str(DataBase.fonctionHachage(totalstr.encode("utf-8")).hexdigest()) != deal.h):
            wrong += [deal.id]
    return wrong
