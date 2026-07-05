#all type of inheritance using match case
class A:
    def showA(self):
        print("Class A")


# Single Inheritance
class B(A):
    def showB(self):
        print("Class B")


# Multilevel Inheritance
class C(B):
    def showC(self):
        print("Class C")


# Hierarchical Inheritance
class D(A):
    def showD(self):
        print("Class D")


# Multiple Inheritance
class E(B, D):
    def showE(self):
        print("Class E")


choice = int(input("""
1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
Enter Choice: 
"""))

match choice:
    case 1:
        print("\nSingle Inheritance")
        obj = B()
        obj.showA()
        obj.showB()

    case 2:
        print("\nMultilevel Inheritance")
        obj = C()
        obj.showA()
        obj.showB()
        obj.showC()

    case 3:
        print("\nHierarchical Inheritance")
        obj1 = B()
        obj2 = D()

        obj1.showA()
        obj1.showB()

        obj2.showA()
        obj2.showD()

    case 4:
        print("\nMultiple Inheritance")
        obj = E()
        obj.showA()
        obj.showB()
        obj.showD()
        obj.showE()

    case _:
        print("Invalid Choice")