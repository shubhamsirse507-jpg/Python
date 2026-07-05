class purchase:
    def __init__(self, buyer, item, unit_price, quantity, purchase_date):
        self.buyer = buyer
        self.item = item
        self.unit_price = unit_price
        self.quantity = quantity
        self.purchase_date = purchase_date

    def total_price(self):
        return self.unit_price * self.quantity

    def display_purchase_details(self):
        return f"""
Buyer         : {self.buyer}
Item          : {self.item}
Unit Price    : {self.unit_price}
Quantity      : {self.quantity}
Purchase Date : {self.purchase_date}
Total Price   : {self.total_price()}
"""


if __name__ == "__main__":
    order = purchase("Alice", "Jeans", 1499, 2, "2026-06-18")
    print(order.display_purchase_details())
