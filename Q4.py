#Reverse of a Number
Num = int(input("Enter a Number: "))
reverse = 0
while Num > 0:
    reminder = Num % 10
    reverse = (reverse * 10) + reminder
    Num = Num // 10
print("Reverse of a Number is ", reverse)
