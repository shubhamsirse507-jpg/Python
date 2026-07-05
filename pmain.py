class p1:

    def xyz(self,name ):
      self.name= name
      print("class xyz")

    def show_p1(self):
       print("show form p1")

    def __init__(self,name):
       self.name=name
       print("p1 con")
       print(self.name)

class p2:
    def abc(self,age):
        self.age=age
        print("class abc")

    def show_p2(slef):
        print("show form p2")

    def __init__(self,age):
       self.age=age
       print("p2 con")
       print(self.age)

class c(p1,p2):
    def pqr(self,year):
        self.yaer=year

    def call_p2_show(self):
       return p2.show(self)

    def __init__(self,name,age):
        print("c con")
        p1.__init__(self,name)
        p2.__init__(self,age)

#object
obj=c("Shubham",20)
obj.xyz("Shubham")
obj.abc(20)
obj.pqr(3)
obj.show_p1()
obj.show_p2()




