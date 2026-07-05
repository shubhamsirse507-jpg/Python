#globalvar="hi"
class demo:
    """
    pass
    msg="hello"
    def __init__(self):
        print("Created!")

    def __init__(self,age):
        self.name="XYZ"
        self.age=age

    def __del__(self):
        print("Deleted!")

    def access_globalvar(self):
        print(globalvar)
        local_var=90
        print(local_var)

obj=demo(20)
print(obj.name)
print(obj.age)
print(obj.msg)
obj.access_globalvar()
print(globalvar) 

"""
#to Display all the data

    def __init__(self,age):
        self.name="XYZ"
        self.age=age

    def display(self):
        print(f"name is {self.name} & age is {self.age}")

obj=demo(20)
obj.display()
