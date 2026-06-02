#Selection for gaverment job
age = int(input("Enter Your Age: "))
Gender = input("Enter Your Gender: ")
Hight = int(input("Enter Your Hight in cm: "))

if age >= 20 and age <= 30 and (Gender == "Male" or Gender == "Female") and Hight >= 120:
    print("You are Eligible For Gaverment Job")
else:
    print("You are not Eligible for Gaverment Job") 