class PersonModel:

    def __init__(self, id: int, last_name: str, first_name: str, public_key: str):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.public_key = public_key

    def __str__(self):
        return str(self.id) + " " + str(self.first_name) + " " + str(self.last_name)

    def toJSON(self):
        JSON = {}
        JSON["id"] = self.id
        JSON["firstName"] = self.first_name
        JSON["lastName"] = self.last_name
        return JSON
