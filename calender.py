#calender
choice = int(input("Enter the yr choice: "))

match choice:
    case 1|2|3|4|5:
        print("Weekday")

    case 6|7:
        print("Weekend")
    
    case _:
        print("Invalid choice")