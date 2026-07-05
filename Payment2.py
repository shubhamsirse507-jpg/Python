class payment:
    def pay(self):
        pass
    print("Payment process started...")

class upi(payment):
    def pay(self):
        return f"payment done ny upi"

class gpay(payment):
    def pay(self):
        return f"payment Done by gpay"

class payment_module:
    def payment_process(self,obj):
        print(obj.pay())

p=payment_module()
print("payment")
print("1.upi\n2.gpay\n3.card\n4.exit")
choice=int(input("Enter yr Choice\n"))
match choice:
    case 1:
        obj=upi()
       # print(u.pay())
    case 2:
        obj=gpay()
        #print(g.pay())
    case 3:
        pass
    case 4:
        exit()
        print("Thankyou for using :)")
    case _:
        print("invalid choice")

p.payment_process(obj)

#multiple obj
obj=[upi(),gpay()]
for i in obj:
    print(i.pay())