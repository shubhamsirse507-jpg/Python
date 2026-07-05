class car:
    model="x1"
class colour(car):
    def show(self,colour):
        self.colour=colour
class brand(colour):
    def disp(self):
        print("BMW",self.colour,self.model)

b=brand()
b.show("red")
b.disp()