import binascii

from flask import Flask, request
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b
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
    config["keys_path"] = configfile["keys"]
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


def fonctionHachage(string: bytes):
    h = BLAKE2b.new()
    h.update(string)
    return h


@app.route('/dev/makeSignature')
def makeSignature():  # /!\ Only for dev environment /!\#
    if checkParams(request.args, ['idSender', 'idReceiver', 'amount']):
        db = dbConnexion()
        idEnvoyeur = request.args.get("idSender")
        idReceveur = int(request.args.get("idReceiver"))
        montant = float(request.args.get("amount"))
        with open(getConfig()["keys_path"], 'r') as file:
            json_object = json.load(file)
        private_key = RSA.import_key(json_object[idEnvoyeur]["privateKey"])
        date = datetime.date.today()
        deal_list = db.getDealList()
        last_hash = ""
        totalstr = str(idEnvoyeur) + str(idReceveur) + str(montant) + str(date)
        if (len(deal_list) > 0):
            last_hash = deal_list[len(deal_list) - 1].h
            totalstr += str(last_hash)
        current_hash = fonctionHachage(totalstr.encode("utf-8"))
        signer = PKCS115_SigScheme(private_key)
        signature = signer.sign(current_hash)
        return {"signature":binascii.hexlify(signature).decode("utf-8")}
    else:
        return "pas les bon arguments"


@app.route('/transactions/add')
def addTransaction():
    db = dbConnexion()
    if checkParams(request.args, ['idSender', 'idReceiver', 'amount', "signature"]):
        idEnvoyeur = int(request.args.get("idSender"))
        idReceveur = int(request.args.get("idReceiver"))
        montant = float(request.args.get("amount"))
        signature = request.args.get("signature")
        signature = binascii.unhexlify(signature.encode("utf-8"))
        public_key = RSA.import_key(db.getPerson(int(idEnvoyeur)).public_key)

        try:
            date = datetime.date.today()
            deal_list = db.getDealList()
            last_hash = ""
            totalstr = str(idEnvoyeur) + str(idReceveur) + str(montant) + str(date)
            if (len(deal_list) > 0):
                last_hash = deal_list[len(deal_list) - 1].h
                totalstr += str(last_hash)
            current_hash = fonctionHachage(totalstr.encode("utf-8"))
            verifieur = PKCS115_SigScheme(public_key)
            verifieur.verify(current_hash, signature)
            db.addTransaction(idEnvoyeur, idReceveur, montant, date, current_hash.hexdigest())
            message = "transaction ajoutée"
        except Exception as exception:
            message = exception.__str__()
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
    db = DataBase(path)
    liste = db.getDeal(int(idTransaction))
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

    # Créations des clé publique et privée
    if checkParams(request.args, ['lastName', 'firstName']):
        try:
            first_name = str(request.args.get("firstName"))
            last_name = str(request.args.get("lastName"))

            # RSA keys
            keys = RSA.generate(1024)
            private_key = keys.exportKey('PEM')
            public_key = keys.publickey().exportKey('PEM')
            # add to database
            db.addPerson(last_name, first_name, public_key.decode())

            # ---add keys to jsonfile /!\ only for dev environment---#
            list = db.getPersonList()
            personAdded = list[len(list) - 1]
            with open(getConfig()["keys_path"], 'r') as file:
                json_object = json.load(file)
            keysDict = {"privateKey": private_key.decode(), "publicKey": public_key.decode()}
            json_object[str(personAdded.id)] = keysDict
            with open(getConfig()["keys_path"], 'w') as file:
                json.dump(json_object, file)
            # -------------------------------------------------------#
            return keysDict
        except Exception as exception:
            return exception
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

@app.route('/getSolde/<idPerson>') #Obtenir le solde d'une personne spécifique
def getSoldeOf(idPerson):
    listeID = {}
    listeID[int(idPerson)] = 0
    return calculSolde(listeID)

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
