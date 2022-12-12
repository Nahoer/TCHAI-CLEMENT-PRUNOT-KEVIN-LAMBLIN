import testv1
import testv2
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

if r.text == "Connexion OK":
    # Show the data integrity
    r = requests.get(base_url + "/verifyIntegrity")
    print("Vérificiation de l'intégrité : ")
    print(r.text)
    print()

    # Call the v2 attack
    print("Attaque : ")
    from src.attack import attackv2

    # Show the data integrity after attack
    r = requests.get(base_url + "/verifyIntegrity")
    print("Vérificiation de l'intégrité : ")
    print(r.text)
