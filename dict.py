#class work
"""
#dict prg
x ={}
print(x.type(x))
#add
x["name"]="ram" 
print(x)
print(x["name"])
#upadte 
x["name"]="sita"
print(x)
x[101]="stus data"
print(x)

#del or pop
del x[101]
print(x)
"""

"""
student = {"name":"ram","age":20,"div":"A"}

print(student.keys())
print(student.values())
print(student.items())

for keys, values in student.items():
    print(keys, values)

product={
    101:(
        "product name":"car",
        "product price":"2023",
        "xolour":"red",
        "qty":10,
        "models":[507,202]
    )
}
print(product[101]["colur"])

#key(
for v in range 

"""
#set
x = set()
print(type(x))

x.add(30)
print(x)

x = {10,20,30,40,10}
print(x)

x1 = list(x)
print(x1[0])

x1[2] = 90
print(x1)

x = set(x1)
print(x, type(x))

A = {1,2,3}
B = {3,4,5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)
 
print(A.difference(B))
print(B - A)

print(A.symmetric_difference(B))
print(A ^ B)    