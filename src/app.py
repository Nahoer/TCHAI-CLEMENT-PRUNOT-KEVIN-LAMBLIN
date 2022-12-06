from flask import Flask, request, redirect
from database import DataBase
from markupsafe import escape

app = Flask(__name__)

def checkParams(requestArgs, list:[str]):
    ok = True
    for param in list:
        if not (param in requestArgs):
            ok=False
    return ok

@app.route('/addTransaction')
def addTransaction():
    db = DataBase("../database/transactions.db")
    message = ""
    if checkParams(request.args, ['idEnvoyeur', 'idReceveur', 'montant', 'date']):
        idEnvoyeur = int(request.args.get("idSender"))
        idReceveur = int(request.args.get("idReceiver"))
        montant = int(request.args.get("amount"))
        date = request.args.get("date")
        db.addTransaction(idEnvoyeur, idReceveur, montant, date)
        print(str(idEnvoyeur) + " " + str(idReceveur) + " " + str(montant) + " " + date)
        return redirect(f"/Transactions")
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "idEnvoyeur: id de l'auteur de la transaction<br/>"
        message += "idReceveur: personne qui reçoit l'argent de la transaction<br/>"
        message += "montant: montant de la transaction<br/>"
        message += "date: date de la transaction"
        return message

@app.route('/Transactions')
def listerTransactions():
    db = DataBase("../database/transactions.db")
    liste = db.getDealList()
    message=""
    for deal in liste:
        message+=str(deal)+"<br/>"
    return message

@app.route('/addPerson')
def addPersonne():                                  #/addPerson?firstName=<firstname>&lastName=<lastname> sans quote pour ajouter
    db = DataBase("../database/transactions.db")

    message = ""
    if checkParams(request.args, ['lastName', 'firstName']):
        first_name = str(request.args.get("firstName"))
        last_name = str(request.args.get("lastName"))
        db.addPerson(last_name, first_name)
        return redirect(f"/Persons")
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "firstName: id de l'auteur de la transaction<br/>"
        message += "lastName: personne qui reçoit l'argent de la transaction"
        return message


@app.route('/Persons')
def listerPersonnes():
    db = DataBase("../database/transactions.db")
    liste = db.getPersonList()
    message=""
    for person in liste:
        message+=str(person)+"<br/>"
    return message

@app.route('/Connexion')
def connexion():
    return "Connexion OK"