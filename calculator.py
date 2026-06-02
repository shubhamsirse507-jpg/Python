print("calculator\n1.add\n2.sub\n3.div\n4.mul\n5.exit\n")
choice = int(input("Enter Yr choice: "))

match choice:
    case 1:
        num1 = int(input("Enter 1st no: "))
        num2 = int(input("Enter 2nd no: "))
        print(f"Add of {num1} and {num2} is {num1+num2}")
        
    case 2:
        num1 = int(input("Enter 1st no: "))
        num2 = int(input("Enter 2nd no: "))
        print(f"Sub of {num1} and {num2} is {num1-num2}")
    case 3:
        num1 = int(input("Enter 1st no: "))
        num2 = int(input("Enter 2nd no: "))
        print(f"div of {num1} and {num2} is {num1/num2}")
    case 4:
        num1 = int(input("Enter 1st no: "))
        num2 = int(input("Enter 2nd no: "))
        print(f"mul of {num1} and {num2} is {num1*num2}")
    case 5:
        print("Exit")
    case _:               #default case
        print("Invalid Choice")