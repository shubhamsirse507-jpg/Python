age = int(input("Enter age: "))
gender = input("Enter gender (Male/Female): ")
ticket_class = input("Enter class (AC/Non-AC): ")

fare = 500

if age >= 60:
    fare = fare - (fare * 0.20)

if gender.lower() == "female":
    fare = fare - (fare * 0.10)

if ticket_class.lower() == "ac":
    fare = fare + 300

print("Final Fare =", fare)
