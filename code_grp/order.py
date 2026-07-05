from payment import payment
from product1 import product
class order (product,payment):
    def bill(self):
        qty=int(input("enter qty: "))
        total=self.price*qty
        print(self.show_product())
        print(self.pay(total))

obj=order("car",5000)
obj.bill()