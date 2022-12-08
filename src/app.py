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
        montant = int(request.args.get("amount"))
        db.addTransaction(idEnvoyeur, idReceveur, montant)
        return message
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "idEnvoyeur: id de l'auteur de la transaction<br/>"
        message += "idReceveur: personne qui reçoit l'argent de la transaction<br/>"
        message += "montant: montant de la transaction<br/>"
        return message


@app.route('/Transactions')
def listerTransactions():
    db = DataBase(path)
    liste = db.getDealList()
    message = ""
    for deal in liste:
        message += str(deal) + "<br/>"
    return message


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


@app.route('/Persons')
def listerPersonnes():
    db = DataBase(path)
    liste = db.getPersonList()
    message = ""
    for person in liste:
        message += str(person) + "<br/>"
    return message


@app.route('/Connexion')
def connexion():
    return "Connexion OK"


@app.route('/TransactionsOrderedByDate')
def listerTransactionsParDate():
    db = DataBase(path)
    liste = db.getDealListFromDate()
    message = ""
    for deal in liste:
        message += str(deal) + "<br/>"
    return message


@app.route('/TransactionsFor')
def listerTransactionPour():
    db = DataBase(path)
    id = -1
    if checkParams(request.args, ['id']):
        id = int(request.args.get("id"))

    if id >= 0:
        message = ""
        liste = db.getDealForUser(id)
        for deal in liste:
            message += str(deal) + "<br/>"
    else:
        message = "Id invalide"

    return message


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
    return str(listeID)
