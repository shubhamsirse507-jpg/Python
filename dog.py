from inheritance import Animal

class Dog(Animal):
    def __init__(self, name="Unknown", weight=0):
        super().__init__(name=name, weight=weight)
        print("child com!")


obj = Dog(name="Buddy", weight=12)
print(obj.type)
print(obj.name)
print(obj.weight)
