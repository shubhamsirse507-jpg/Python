class Account:
    def __init__(self, bal):
        self._bal = bal

    def get_bal(self):
        print("Current Balance:", self._bal)

    def deposit(self, amt):
        self._bal += amt
        print("Deposited:", amt)
        print("New Balance:", self._bal)

    def withdraw(self, amt):
        if amt <= self._bal:
            self._bal -= amt
            print("Withdrawn:", amt)
            print("Remaining Balance:", self._bal)
        else:
            print("Insufficient Balance!")

    def set_bal(self, amt):
        self._bal = amt
        print("Balance Updated:", self._bal)


obj = Account(5000)

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    match choice:
        case 1:
            obj.get_bal()

        case 2:
            amt = int(input("Enter amount to deposit: "))
            obj.deposit(amt)

        case 3:
            amt = int(input("Enter amount to withdraw: "))
            obj.withdraw(amt)

        case 4:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")