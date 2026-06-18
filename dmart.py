class Grocery:
    def __init__(self, section, item, price, qty, brand, exp_date):
        self.section = section
        self.item = item
        self.price = price
        self.qty = qty
        self.brand = brand
        self.exp_date = exp_date

    def display_grocery_details(self):
        return f"""
Section : {self.section}
Item    : {self.item}
Price   : {self.price}
Qty     : {self.qty}
Brand   : {self.brand}
Expiry  : {self.exp_date}
"""