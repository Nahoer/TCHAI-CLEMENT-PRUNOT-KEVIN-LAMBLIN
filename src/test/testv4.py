import binascii

from flask import Flask, request
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import datetime
import requests
import json

base_url = "http://127.0.0.1:5000"
with open('../../utils/config.json', 'r') as openfile:
    json_object = json.load(openfile)

with open('../../utils/config.json', 'w') as openfile:
    json_object["database"] = "test"
    json.dump(json_object, openfile)

response = requests.get(base_url + "/persons")
persons = response.json()
print()
print(str(len(persons)) + " personnes dans la base de données")
print()
print("Ajout d'une nouvelle personne")
print()
response = requests.get(base_url + "/persons/add?lastName=Mechant&firstName=Hackeur")
keys = response.json()
response = requests.get(base_url + "/persons")
persons = response.json()
print(str(len(persons)) + " personnes dans la base de données")
print()
print("Tentative de voler de l'argent à Macron:")
id = persons[len(persons) - 1]["id"]
idOther = 6
amount = 50000
print(requests.get(
    base_url + "/transactions/add?idSender={idOther}&idReceiver={id}&amount={amount}".format(id=id, idOther=idOther,
                                                                                             amount=amount)).text)
print(requests.get(
    base_url + "/transactions/add?idSender={idOther}&idReceiver={id}&amount={amount}&signature=013123123123123123123123123123".format(
        id=id, idOther=idOther, amount=amount)).text)
idEnvoyeur = id
idReceveur = idOther
amount = float(amount)
private_key = RSA.import_key(keys["privateKey"])
date = datetime.date.today()
deal_list = requests.get(base_url + "/transactions").json()
last_hash = ""
if (len(deal_list) > 0):
    last_hash = deal_list[len(deal_list) - 1]["hash"]
totalstr = str(idEnvoyeur) + str(idReceveur) + str(amount) + str(date) + str(last_hash)
current_hash = BLAKE2b.new()
current_hash.update(totalstr.encode("utf-8"))
signer = PKCS115_SigScheme(private_key)
signature = signer.sign(current_hash)
signature = binascii.hexlify(signature).decode("utf-8")
print(requests.get(
    base_url + "/transactions/add?idSender={id}&idReceiver={idOther}&amount={amount}&signature={signature}".format(
        id=id, signature=signature, amount=amount, idOther=idOther)).text)
print()
print("hash faux:")
print(requests.get(base_url + "/verifyIntegrity").text)
