
try:
    a=int(input("Entre a number"))
    b=int(input("Entre a number"))
    print("divi",a/b)
except ArithmeticError as q:
    print("No",q)



try:
    a=("name:ram")
    print(a["name"])
    print(a["ram"])
except Exception as e:
    print(e)
else :
    print("end")
