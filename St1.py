str = "Mharashatra"
# Print all characters
print(str[::1])
# Print only characters at odd indexes (1, 3, 5, ...)
print(str[6::10])

#print vowel's
text = "Savedita"
vowel = "aeiouAEIOU"

for ch in text :
    if ch in vowel :
        print(ch)

#even & odd

#  
print(text[::2])
print(len(text))

#reverse
x ="maha"
rev = ""
for ch in x:
    rev= ch +rev
    print(rev)

# list prg
y = [1,2,3,4,5]
print(y)
y[2]=50
print(y)

print(len(y))
print(sum(y))
print(min(y))
print(max(y))

#square of list
b = [10,20,30,40]
s=0
for i in b:
    s= s + i*i
print("sum of square:",s)

#Even and odd
list =[21,32,65,25,5]
s=0
for i in list:
    if i %2 == 0:
        list
        print(0)
    else:
        print(1)

#get the input from user
i=[]
for i in range(5):
    print(f"ENter {i+1} element : ")
    ip =int(input())
    x =x+[ip]
    print(x)