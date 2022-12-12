import requests
import json

base_url = "http://127.0.0.1:5000"
with open('../../utils/config.json', 'r') as openfile:
    json_object = json.load(openfile)

with open('../../utils/config.json', 'w') as openfile:
    json_object["database"] = "test"
    json.dump(json_object, openfile)
# Make a connexion test with the flask server
r = requests.get(base_url + "/connexion")

print(r.text)

# If the server is correctly connected, we process the test
if r.text == "Connexion OK":
    # First we get the list of persons registered in our database
    r = requests.get(base_url + "/persons")
    print("Liste des personnes : ")
    print(r.text)
    print()

    #getSolde of 1
    print("Solde de 1:")
    r = requests.get(base_url + "/getSolde/1")
    print(r.text)
    print()
    # Add a new person in the database
    print("Ajout d'une personne : ")
    r = requests.get(base_url + "/persons/add?firstName=Marie&lastName=JEANNE")
    print(r.text)
    print()

    # Show list of persons again
    print("Liste des personnes : ")
    r = requests.get(base_url + "/persons")
    print(r.text)
    print()

    # Show the list of actual deals in the database ordered by date
    print("Liste des transactions par date : ")
    r = requests.get(base_url + "/transactions/date")
    print(r.text)
    print()

    # Add a new deal
    print("Ajout d'une transaction : ")
    print("1 envoie 50 à 2")
    r = requests.get(base_url + "/transactions/add?idSender=1&idReceiver=2&amount=50")
    print(r.text)
    print()

    # Show again the list of deals ordered by date
    print("Liste des transactions par date : ")
    r = requests.get(base_url + "/transactions/date")
    print(r.text)
    print()

    # Show deal for a person
    print("Liste des transactions pour la personne 1 : ")
    r = requests.get(base_url + "/transactions/1")
    print(r.text)
    print()

    # Show the amount of a person
    print("La personne avec l'id 1 a un montant de : ")
    r = requests.get(base_url + "/getSolde/1")
    print(r.text)

else:
    print("Le serveur Flask ne fonctionne pas actuellement sur l'adresse : " + base_url)
