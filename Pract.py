class student:
    name = "Shubham"

class Marks(student):
    age =20
    marks = 90
s1 = student()
s2 = Marks()
print(f"name:{s2.name} \nage: {s2.age}  \nmarks: {s2.marks}")
