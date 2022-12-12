import requests

base_url = "http://127.0.0.1:5000"

# Show the list of deals ordered by date
print("Liste des transactions par date avec la modification: ")
r = requests.get(base_url + "/transactions")
print(r.text)
print()

# Show the list of deals ordered by date
print("Le pirate crée une trasaction vers son compte: ")
r = requests.get(base_url + "/transactions/add?idSender=1&idReceiver=3&amount=5000")
print(r.text)
print()

# Show again the list of deals ordered by date
print("Liste des transactions par date : ")
r = requests.get(base_url + "/transactions")
print(r.text)
