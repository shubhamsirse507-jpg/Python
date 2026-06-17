
#1 - 100  -> %5 -> sum -> square
i = 1
sum = 0
while i <= 100:
    if i % 5 == 0:
        sum += i
    i += 1

square = sum ** 2
for i in range(1, 101):
    if i % 5 == 0:
        sum +=i
print("Sum:", sum)
print("Square of the sum is:", square)

# 5 table 
n= 5
for i in range(1, 11):
    print(n, "x" , i , "=" , n*i)