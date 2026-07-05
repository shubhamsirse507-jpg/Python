from dimart import Grocery
from clothes import Clothes

g = Grocery(
    "grocery_section",
    "sugar",
    60,
    100,
    "Sugarlite",
    "2026-06-01"
)

c = Clothes(
    "clothing_section",
    "Jeans",
    1499,
    "XL",
    "Levis"
)

while True:
    print("\nWelcome to D-Mart")
    print("1. Grocery Section")
    print("2. Clothing Section")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            print(g.display_grocery_details())

        case 2:
            print(c.display_clothes_details())

        case 3:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")