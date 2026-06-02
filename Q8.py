#Finding No is Palidrom or not
a = int(input("Enter a number: "))
temp = a
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10
if a == reverse:
    print(a, "is a palindrome number")
else:
    print(a, "is not a palindrome number")
    