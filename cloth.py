class Cloth:
    def __init__(self, section, item, price, size, brand):
        self.section = section
        self.item = item
        self.price = price
        self.size = size
        self.brand = brand

    def display_cloth_details(self):
        return f"""
Section : {self.section}
Item    : {self.item}
Price   : {self.price}
Size    : {self.size}
Brand   : {self.brand}
"""
