
#1 - 100  -> %5 -> sum -> square
print("option 1 : for find sum of square")
print("option 2 : for find table of any no")
print("oprion 3 : for fing sum of given square")
op=int(input("Enter option: "))

if op == 1 :

    i=int(input("Enter a no: "))
    sum = 0
    while i <= 100:
            if i % 2 == 0:
                sum += i
            i += 1
            print(i)

elif op == 2:
    #find sum of square
    a = int(input("Enter "))
    sum = 0
    square = sum ** 2
    for i in range(1, 101):
        if i % 5 == 0:
            sum +=i
    print("Sum:", sum)
    print("sum is:", square)
elif op == 3:
# 5 table 

    num=int(input("Enter a No to get table of No : "))
    for i in range(1 , 11):
        print(num,"x",i,num*i)
        #O/p ex : n=5 & i = no btw 1 to 10 = n*i = 5*2 = 10
        