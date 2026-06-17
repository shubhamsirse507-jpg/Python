#print even no rom 23 to 57 in reverse order
i = 57 
while i >= 23:
    if i in range (57 ,23, -1):
        if i % 2 == 0:
            print(i)
    i-= 1

    