try:
    file=open("myfile.txt","x")
    print(file)
except Exception as e:
    print(e)

#add
with open("myfile.txt","w") as f:
    f.write("hello")
    print("data added")
#read
with open("myfile.txt","r")as f:
    data=f.read()
    print(data)
#append
with open("myfile.txt","a")as f:
    f.write("\nnew sentance")