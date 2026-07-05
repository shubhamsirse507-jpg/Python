from Bank import Bank 
class Account:
    def __init__(self, Accounttype,Acno,Aholder):
        self.Accounttye="Saving Account"
        self.Acno="195369532"
        self.Aholder="PavanKumar Panday"
        print(self.Accounttye, self.Acno , self.Aholder)

obj=Account(Accounttype="Saving Account",Acno="195369532",Aholder="PavanKumar Panday")
obj=Bank(name="icici",add="\nChikhali")
