
class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_bank_info(self):
        print(f"Bank: {self.name}")
        print(f"Address: {self.address}")


class SavingsAccount(Bank):
    def __init__(self, name, address, account_number, balance=0, interest_rate=4.0):
        super().__init__(name, address)
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Cannot withdraw. Check balance or amount.")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest on savings: {interest}")
        return interest


class CurrentAccount(Bank):
    def __init__(self, name, address, account_number, balance=0, overdraft_limit=1000):
        super().__init__(name, address)
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Cannot withdraw. You reached the overdraft limit.")

    def display_overdraft(self):
        print(f"Overdraft limit: {self.overdraft_limit}")


if __name__ == '__main__':
    print("=== Student Example: Bank Hierarchical Inheritance ===")
    print("I am a student writing this code to show how classes inherit from a base class.")

    savings = SavingsAccount("My Bank", "21 School Road", "SAV123", balance=5000)
    savings.display_bank_info()
    print(f"Account number: {savings.account_number}")
    savings.deposit(1500)
    savings.withdraw(2000)
    savings.calculate_interest()

    print("\n---")

    current = CurrentAccount("My Bank", "21 School Road", "CUR456", balance=2000, overdraft_limit=3000)
    current.display_bank_info()
    print(f"Account number: {current.account_number}")
    current.deposit(1000)
    current.withdraw(4500)
    current.display_overdraft()

   