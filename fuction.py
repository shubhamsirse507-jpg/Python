"""
def add(a,b):
    return a+b
print(add(10,20))

#print(add(12.3,3,10.2))
"""
# exception hand
"""
try:
    ip=int(input("Entre a number"))
    print(ip)
except ValueError:
    print("Enter number only")
"""
#input fron user
"""
try:
    a=int(input("Entre a number"))
    b=int(input("Entre a number"))
    print("divi",a/b)
except ValueError as e:
    print(e)
except ArithmeticError as q:
    print(q)
"""

try:
    a=("name:ram")
    print(a["name"])
    print(a["ram"])
except Exception as e:
    print(e)
else :
    print("end")

"""
#task
try:
    a=int(input("Enter f1: "))
    b=int(input("Enter f2: "))
    def add(a,b):
        print("sum is:",a + b)
except ValueError as e:
        print("Enter Values only")
else:
    print("End")
"""
#oop concept

#4 p
"""
1. inheritance
2. polymorphism 
3. abstraction
4. encapsulation
"""



