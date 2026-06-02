#Find Armstrong Number or not
num = int(input("Enter a Number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10 #Extract the last digit
    sum += digit ** 3 #Add the cube of the digit to the sum
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")