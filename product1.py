class product:
    def __init__(self,name,price):
        self.name= name
        self.price= price

    def show_product(self):
        return f"product: {self.name}\nprice: {self.price}"