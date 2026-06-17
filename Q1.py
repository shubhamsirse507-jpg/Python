#finding Largest in three numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if a> b and a>c:
    print("Largest no is ", a)
elif b>a and b>c:
    print("Largest no is ", b)
elif c>a and c>b:
    print("Largest no is ", c)
else:
    print("All are equal")