import requests

base_url = "http://127.0.0.1:5000"

# Make a connexion test with the flask server
r = requests.get(base_url + "/Connexion")
print(r.text)

# If the server is correctly connected, we process the test
if r.text == "Connexion OK":
    # First we get the list of persons registered in our database
    r = requests.get(base_url + "/Persons")
    print("Liste des personnes : ")
    print(r.text)
    print()

    # Add a new person in the database
    print("Ajout d'une personne : ")
    r = requests.get(base_url + "/addPerson?firstName=Marie&lastName=JEANNE")
    print(r.text)
    print()

    # Show list of persons again
    print("Liste des personnes : ")
    r = requests.get(base_url + "/Persons")
    print(r.text)
    print()

    # Show the list of actual deals in the database ordered by date
    print("Liste des transactions par date : ")
    r = requests.get(base_url + "/TransactionsOrderedByDate")
    print(r.text)
    print()

    # Add a new deal
    print("Ajout d'une transaction : ")
    r = requests.get(base_url + "/addTransaction?idSender=1&idReceiver=2&amount=50")
    print(r.text)
    print()

    # Show again the list of deals ordered by date
    print("Liste des transactions par date : ")
    r = requests.get(base_url + "/TransactionsOrderedByDate")
    print(r.text)
    print()

    # Show deal for a person
    print("Liste des transactions pour la personne 1 : ")
    r = requests.get(base_url + "/TransactionsFor?id=1")
    print(r.text)
    print()

    # Show the amount of a person
    print("La personne avec l'id 1 a un montant de : ")
    r = requests.get(base_url + "/getSolde?idPerson=1")
    print(r.text)

else:
    print("Le serveur Flask ne fonctionne actuellement sur l'adresse : " + base_url)
