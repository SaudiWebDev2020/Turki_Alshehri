class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.transferList = {}

    def make_deposite(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:",self.name,"Balance: $"+str(self.account_balance))
        return self

    def  transfer_money(self, other_user_account_ID, amount):
        self.transferList[other_user_account_ID] = amount
        self.account_balance -= amount
        return self


turki = User("Turki", "abcde@gmail.com").make_deposite(700).display_user_balance().make_withdrawal(150).display_user_balance().transfer_money(1234,500).display_user_balance().transfer_money(9087, 10)

print(turki.transferList)