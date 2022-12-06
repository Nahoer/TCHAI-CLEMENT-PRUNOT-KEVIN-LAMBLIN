from flask import Flask, request, redirect
from database import DataBase
from markupsafe import escape

app = Flask(__name__)


@app.route('/addTransaction')
def addTransaction():
    db = DataBase("../database/transactions.db")
    idEnvoyeur = int(request.args.get("idSender"))
    idReceveur = int(request.args.get("idReceiver"))
    montant = int(request.args.get("amount"))
    date = request.args.get("date")
    message = ""
    if(idEnvoyeur=="" or idReceveur=="" or montant=="" or date==""):
        message = "Veuillez founir les données suivante :\n"
        message += "idEnvoyeur: id de l'auteur de la transaction\n"
        message += "idReceveur: personne qui reçoit l'argent de la transaction\n"
        message += "montant: montant de la transaction\n"
        message += "date: date de la transaction"
    else:
        db.addTransaction(idEnvoyeur, idReceveur, montant, date)
        print(str(idEnvoyeur)+" "+str(idReceveur)+" "+str(montant)+" "+date)
        message = "Transaction ajoutée"
        liste = db.getDealList()
        for deal in liste:
            print(deal)
    return message

@app.route('/addPerson')
def addPersonne():                                  #/addPerson?firstName=<firstname>&lastName=<lastname> sans quote pour ajouter
    db = DataBase("../database/transactions.db")
    first_name = str(request.args.get("firstName"))
    last_name = str(request.args.get("lastName"))
    message = ""
    if not first_name or not last_name:
        message = "Veuillez founir les données suivante :\n"
        message += "firstName: id de l'auteur de la transaction\n"
        message += "lastName: personne qui reçoit l'argent de la transaction"
    else:
        db
        #db.addPerson(last_name, first_name)
    return redirect(f"/Persons")


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