dict1 = {
    101:{
        "Name":"ram",
        "Age":20,
        "sub":("py","java","mern"),
        "marks":(90,89,78)
    },
        102:{
        "Name":"sita",
        "Age":19,
        "sub":("py","java","mern"),
        "marks":(70,80,78)
    },
        103:{
        "Name":"rahul",
        "Age":21,
        "sub":("py","java","mern"),
        "marks":(70,35,45)
    },
        104:{
        "Name":"gita",
        "Age":20,
        "sub":("py","java","mern"),
        "marks":(70,26,92)
    }
}
#Format
Roll = 0
for i in dict1:
    Roll = i
    print(i,dict1[i]["Name"],dict1[i]["Age"],dict1[i]["sub"],dict1[i]["marks"])
#Find Top_1 Student
top_1 =0
name = ""
Roll = 0

for i in dict1:
    total=sum(dict1[i]["marks"])

    if total > top_1:
        top_1 = total
        name = dict1[i]["Name"]
        Roll = i

print("Roll is : ",Roll)
print("top Stdent is : ", name)
print("marks: ", top_1)

#Count Of All Stud
count =len(dict1)
print("Total student : ", count)

#Name of Stud who's Age is >= 19
for i in dict1:
    if dict1[i]["Age"] >=19:
        print(i,dict1[i]["Name"],dict1[i]["Age"])
