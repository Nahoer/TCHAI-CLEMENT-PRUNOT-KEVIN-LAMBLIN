class PersonModel:

    def __init__(self, id:int, last_name:str, first_name:str):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return str(self.id)+" "+str(self.first_name)+" "+str(self.last_name)
