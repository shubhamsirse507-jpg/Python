
#star pattern
a = 4
for i in range (1, 4+1):
        for j in range (1, 4+1):
            print("*", end=" ")
        print()

 #ox pattern

b = 4
for i in range (1, 4+1):
        print("x" ," ", "o"," ", "x")
        print()


for i in range (1, 6, 2):
    print(str(i) * ((i+1)//2))   

ch = "a" , "b" , "c"
count  = 3
for i in ch :
    print (i * count)
    count-=1

# Upper part
space = 4

for i in range(1, 6, 2):
    print(" " * space + str(i) * i)
    space -= 1

# Lower part
space = 3 

for i in range(3, 0, -2):
    print(" " * space + str(i) * i)
    space += 1

