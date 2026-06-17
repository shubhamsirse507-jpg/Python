#List and Tuple 
products = [ [1, "pen", 10],[2, "pencil", 20],[3, "book", 30]]

n = int(input("Enter no of product: "))

for i in range(n):
    pid = int(input("Enter product id: "))
    name = input("Enter name of product: ")
    price = int(input("Enter product price: "))

    products.append([pid, name, price])

print("\nProduct List")

for product in products:
    print(product)

  
#upadte 
products = [ [1, "pen", 10],[2, "pencil", 20],[3, "book", 30]]

search_p=input("Enter product name to search: ")
if search_p == "pen" and "pencil" and "book":
    print("Product search Succful:)")
else :
    print("Serach is faild:(")

    pid = int(input("Enter product id: "))
    for product in products:
        if product[0] == pid:
                product[1] = input("Enter name of product: ")
                product[2]= int(input("Enter product price: "))

                products.append([pid, name, price])

        print("\nProduct List")

        for product in products:
            print(product) 

#tuple 
product1 = ((1,"Car",567),(2,"truck",345),(3,"bike",200))
print(product1)
x = list(product1)
print(product1)

#itartion on list and tuple 
a =((1,2,3),10,30,["hello"])

for i in x:
    if type(i)==tuple or type(i)==list:
        for item in i:
            print(item)
    else:
        print(i)