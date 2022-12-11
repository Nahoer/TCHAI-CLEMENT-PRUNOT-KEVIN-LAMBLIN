from flask import Flask, request
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from asymetric_crypto import Asymetric_Crypto
from database import DataBase
import hashlib
import datetime
import json

app = Flask(__name__)

def getPath():
    config = json.load(open("../utils/config.json"))
    config = {}
    #config["keys_path"] = configfile["keys"]
    config["db_path"] = database[configfile["database"]]
    return config
def checkParams(requestArgs, list: [str]):
    # Vérifie que tous les paramètres de requête passés en paramètre sont dans la liste d'argument de la requête
    ok = True
    for param in list:
        if not (param in requestArgs):
            ok = False
    return ok
def dbConnexion():
    return DataBase(getConfig()["db_path"])
def fonctionHachage(string:bytes):
    return hashlib.md5(string)
@app.route('/transactions/add')
def addTransaction():
    db = dbConnexion()
    if checkParams(request.args, ['idSender', 'idReceiver', 'amount', "privateKey"]):
        idEnvoyeur = int(request.args.get("idSender"))
        idReceveur = int(request.args.get("idReceiver"))
        montant = float(request.args.get("amount"))

        public_key = RSA.import_key(db.getPerson(int(idEnvoyeur)).public_key)
        private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCGM3CeLKg2DtWh0qVXSnLndrH9frPMeUAELuSF61XNlOQq/TRo\nGe1lNVYoNUE03dUqV/Yf92j+Wzcp7hu6IPGNE70/fthQm5KiBVgMUhgDDw4uRmRO\n9gBV2H0FsHanzTduaqkT7mObVdE/WBnYJEd48wAzAxRZdylpR2lqNCbgMwIDAQAB\nAoGACXh93RvHrzDy0J29/2AIpd8RhpM3exmfc+wfQnguMPjt9T6zQRl7UGYoM2Q2\nutVg4sEcZHsgVLr5NKNSH5uNkE4HAE6dmgSfEdb50jSwFCQa954IMomhYzxsjrcs\nLtM8mimBzAOlFgEiGf9nyjmJYp3/a/cFV1vG4mtFx14FYVkCQQC2J0eJBvmiDrta\nzpL6Zc/kIoEfXXNJ0vNYpEAfpH7qTh+LSzAyHOBeQ+Fj07WRthAAj6okbbDNnCAD\nvslCVsdFAkEAvJtuC73ug6rXxi0VIOHsFho+AckcHG8YHhuStncphwEkd6P9q7h/\nLOexc4nZqB8LqKdx/DESUk4CPWafLzYlFwJAL+2N6QQo0vdFXNNV4QTA+qoJh5Mz\nLo2O8hflt2205zm/Gwuhls36S1NZDsc50ykwdLVYc1VZXABkfBfLJOVocQJBAI+6\nxw8Nq7ENRagRfRN096wUTYKg1tpYUwHGs3R3tN7cIQVHpK3zSH9ZBaLtvz/egM0C\n5dtxLewo5I4UIWUiFvsCQB3tzW4+x5m4QCbfriPq6+sgMJ3CXAmUvRPrdprSbLMc\n+aICAcEkBOPLvnI6DRc9UiHfy+lGnbNEnze8PE83bnw=\n-----END RSA PRIVATE KEY-----"
        param_private_key = request.args.get("privateKey")
        """for i in range(len(param_private_key)):
            if param_private_key[i] == " " and i>31 and i < len(param_private_key)-30:
                private_key+="+"
            else:
                private_key+= param_private_key[i]"""
        """print(len(private_key))
        print(private_key)
        print(db.getPerson(int(idEnvoyeur)).public_key)"""
        private_key = RSA.import_key(private_key) #crash

        date = datetime.date.today()
        deal_list = db.getDealList()

        last_hash = deal_list[len(deal_list)-1].h
        totalstr = str(idEnvoyeur)+str(idReceveur)+str(montant)+str(date)+str(last_hash)

        current_hash = fonctionHachage(totalstr.encode("utf-8")).hexdigest()
        crypteur = Asymetric_Crypto(current_hash, public_key, "md5")
        crypteur.encrypt()
        if crypteur.verify_signature(private_key):
            #db.addTransaction(idEnvoyeur, idReceveur, montant, date, current_hash)
            message = "transaction ajoutée"
        else:
            message = "Erreur de signature"
        return message
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "idEnvoyeur: id de l'auteur de la transaction<br/>"
        message += "idReceveur: personne qui reçoit l'argent de la transaction<br/>"
        message += "montant: montant de la transaction<br/>"
        return message
@app.route('/transactions')
def listerTransactions():
    db = dbConnexion()
    liste = db.getDealList()
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab
@app.route('/transactions/<idTransaction>')
def getTransaction(idTransaction):
    db = dbConnexion()
    liste = db.getDeal(int(idTransaction))
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab


@app.route('/transactions/<idTransaction>')
def getTransaction(idTransaction):
    path = getPath()
    db = DataBase(path)
    liste = db.getDeal(int(idTransaction))
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab


@app.route('/persons/add')
def addPersonne():  # /persons/add?firstName=<firstname>&lastName=<lastname> sans quote pour ajouter
    db = dbConnexion()
    #Créations des clé publique et privée


    if checkParams(request.args, ['lastName', 'firstName']):
        first_name = str(request.args.get("firstName"))
        last_name = str(request.args.get("lastName"))
        keys = RSA.generate(1024)
        private_key = keys.exportKey('PEM')
        public_key = keys.publickey().exportKey('PEM')
        db.addPerson(last_name, first_name, public_key.decode())
        return {"privateKey": private_key.decode()}
    else:
        message = "Veuillez founir les données suivante :<br/>"
        message += "firstName: Prénom de la personne<br/>"
        message += "lastName: Nom de la personne"
        return message

@app.route('/transactions/date')
def listerTransactionsParDate():
    db = dbConnexion()
    liste = db.getDealListFromDate()
    tab = []
    for deal in liste:
        tab += [deal.toJSON()]
    return tab
@app.route('/persons')
def listerPersonnes():
    db = dbConnexion()
    liste = db.getPersonList()
    tab = []
    for person in liste:
        tab += [person.toJSON()]
    return tab

@app.route('/persons/<idPerson>')
def getPerson(idPerson):
    db = dbConnexion()
    person = db.getPerson(int(idPerson))
    tab = [person.toJSON()]
    return tab
@app.route('/connexion')
def connexion():
    return "Connexion OK"
@app.route('/transactions/person/<idPerson>')
def listerTransactionPour(idPerson):
    db = dbConnexion()
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


@app.route('/getSolde/<idPerson>')  # Obtenir le solde d'une personne spécifique
def getSoldeOf(idPerson):
    listeID = {}
    listeID[int(idPerson)] = 0
    return calculSolde(listeID)

@app.route('/getSolde')  # Obtenir le solde de tout le monde
def getSoldes():
    db = dbConnexion()
    listeDeal = db.getDealList()
    listePersons = db.getPersonList()
    listeID = {}
    for person in listePersons:
        listeID[person.id] = 0
    return calculSolde(listeID)

def calculSolde(listeID: dict):  # Fonction générique pour calculer le solde
    path = getPath()

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
    db = DataBase(getPath())
    deals = db.getDealList()
    wrong = []
    for i in range(len(deals)):
        totalstr = str(deals[i].debtor) + str(deals[i].receiver) + str(deals[i].amount) + str(deals[i].date)
        if i > 0:
            totalstr += deals[i - 1].h
        hashAttendu = str(DataBase.fonctionHachage(totalstr.encode("utf-8")).hexdigest())
        if hashAttendu != deals[i].h:
            wrong += [deals[i].id]
    return wrong
