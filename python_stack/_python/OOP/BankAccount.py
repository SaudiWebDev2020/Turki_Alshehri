class BankAccount:

    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate / 100

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print("Balance: $"+str(self.balance))

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.interest_rate * self.balance + self.balance



account1 = BankAccount(1,200)
account1.display_account_info()
account1.yield_interest()
account1.display_account_info()