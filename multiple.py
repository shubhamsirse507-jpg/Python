class father:
    def phone(self):
        print(f"iphone ")

    def show_phone(self,name):
        self.name=name
        print(f"phone nmae is",self.phone)

class son:
    def macbook(self):
        print(f" macbook")

    def show_laptop(self,name):
        self.name=name
        print(f"kaptop name is : ",self.macbook)


class price(father,son):
    def show(self,phone,macbook):
        self.phone=phone
        self.macbook=macbook

obj=price()
obj.phone()
obj.macbook()
obj.show("Iphone","macbook")
obj.show_phone("iphone")
obj.show_laptop("macbook")