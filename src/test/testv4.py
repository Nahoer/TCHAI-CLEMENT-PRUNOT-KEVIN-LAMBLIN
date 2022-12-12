import testv1
import testv2
import testv3
import requests
import json

base_url = "http://127.0.0.1:5000"
with open('../../utils/config.json', 'r') as openfile:
    json_object = json.load(openfile)

with open('../../utils/config.json', 'w') as openfile:
    json_object["database"] = "test"
    json.dump(json_object, openfile)

response = requests.get(base_url + "/persons/add?lastName=Mechant&firstName=Hackeur")
keys = response.json()
print(keys)