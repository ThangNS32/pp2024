class Person:
    def __init__(self,PersonID,Name,DoB):
        self._PersonID = PersonID
        self._Name = Name 
        self._DoB = DoB

    def __str__(self):
        return "ID: {}, Name: {}, DoB: {}".format(self._PersonID,self._Name,self._DoB)
    
    def input(self,get_string_input):
        self._PersonID = get_string_input("Enter ID: ")
        self._Name = get_string_input("Enter Name: ")
        self._DoB = get_string_input("Enter DoB: ")

    def list(self):
        return str(self)
    