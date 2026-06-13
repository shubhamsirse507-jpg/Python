""""
name = "ram" 
print(name)
# return index char 
print(name[0])
# return memory refreence 
print(id(name))
# scling:var name [start index: end index : update ]-->
print(name[1:3])
#string performed
new_name = "p"+name[1:3]
print(new_name)
"""
str= "Mharashatra"
print(str[0:4])
print(str[6:10])
#return even index char
print(str[::2])
#revers Index
print(str[::-1])
print(len(str))
print(str.upper())
print(str.lower())
s="hello i am a student"
print(s.title())   #fuction are independent #caling without refernce
x= "MAharashtra"
for ch in x:
    print(ch,end=" ")