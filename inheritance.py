class Animal:
    type = "animaltype"

    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight
        print("Default animal com")

    def xyz(self):
        print("hello i am from parent class")

    def greet(self):
        print("hello i am Animal")
