class PersonModel:

    def __init__(self, id:int, name:str, first_name:str):
        self.id = id
        self.name = name
        self.first_name = first_name

    def __str__(self):
        return str(self.id)+"|"+str(self.first_name)+"|"+str(self.name)
