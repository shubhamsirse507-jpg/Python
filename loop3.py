uno =int(input("Enter the no: "))
eno =int(input("Enter the no:"))
for i in range (uno , eno+1):
    if i %12 == 0 and i % 15 == 0 and i %19 == 0:
            print(i)
    else:
            print("Enter valid no")
