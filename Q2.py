#Finding Character is capital, small or any other symbol
ch = input("Enter a Character: ")
if ch.isupper():
    print("Cha is Capital", ch)
elif ch.islower():
    print("Cha is Small", ch)
else:
    print("Cha is other Symbol", ch)