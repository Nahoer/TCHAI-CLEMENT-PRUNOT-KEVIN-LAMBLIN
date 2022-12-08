import datetime

from flask import Flask, request, redirect
from database import DataBase
from markupsafe import escape

app = Flask(__name__)
path = "../database/transactions.db"
def checkParams(requestArgs, list: [str]):
    # Vérifie que tous les paramètres de requête passés en paramètre sont dans la liste d'argument de la requête
    ok = True
    for param in list:
        if not (param in requestArgs):
            ok = False
    return ok


@app.route('/transactions/add')
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

@app.route('/transactions/<idTransaction>')
def getTransaction(idTransaction):
    db = DataBase(path)
    liste = db.getDeal(int(idTransaction))
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab

@app.route('/persons/add')
def addPersonne():  # /persons/add?firstName=<firstname>&lastName=<lastname> sans quote pour ajouter
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

@app.route('/transactions/date')
def listerTransactionsParDate():
    db = DataBase(path)
    liste = db.getDealListFromDate()
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab

@app.route('/persons')
def listerPersonnes():
    db = DataBase(path)
    liste = db.getPersonList()
    tab = []
    for person in liste:
        tab += [person.toJSON()]
    return tab
@app.route('/persons/<idPerson>')
def getPerson(idPerson):
    db = DataBase(path)
    liste = db.getPerson(int(idPerson))
    tab = []
    for person in liste:
        tab += [person.toJSON()]
    return tab

@app.route('/connexion')
def connexion():
    return "Connexion OK"


@app.route('/transactions/<idPerson>')
def listerTransactionPour(idPerson):
    db = DataBase(path)
    id = int(idPerson)

    if id >= 0:
        message = ""
        liste = db.getDealForUser(id)
        tab = []
        for deal in liste:
            tab += [deal.toJSON()]
        return tab
    else:
        return "Id invalide"

@app.route('/getSolde/<idPerson>') #Obtenir le solde d'une personne spécifique
def getSoldeOf(idPerson):
    listeID = {}
    listeID[int(idPerson)] = 0
    return calculSolde(listeID)

@app.route('/getSolde') #Obtenir le solde de tout le monde
def getSoldes():
    db = DataBase(path)
    listeDeal = db.getDealList()
    listePersons = db.getPersonList()
    listeID = {}
    for person in listePersons:
        listeID[person.id] = 0
    return calculSolde(listeID)
def calculSolde(listeID:dict): #Fonction générique pour calculer le solde
    db = DataBase(path)
    listeDeal = db.getDealList()
    for id in listeID:
        for deal in listeDeal:
            if deal.debtor == id:
                listeID[id] -= deal.amount
            elif deal.receiver == id:
                listeID[id] += deal.amount
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
