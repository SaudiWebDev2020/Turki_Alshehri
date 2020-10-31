class BankAccount:

    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.interest_rate * self.balance + self.balance



class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account =  BankAccount(interest_rate= 0.02, balance=0)

    def make_deposite(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User:",self.name, ", Balance: $" + str(self.account.display_account_info()))
        return self

        

turki = User("Turki", "ghsd@gmail.com")
turki.account.deposit(1050)
turki.display_user_balance()
turki.account.withdraw(96)
turki.display_user_balance()
print(turki.account.balance)