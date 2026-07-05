
try:
    a=int(input("Entre a number"))
    b=int(input("Entre a number"))
    print("divi",a/b)
except ArithmeticError as q:
    print("No",q)
