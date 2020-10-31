class User:
    
    def __init__(self,name, email, age):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.transferList = {}

    def make_deposite(self, amount):
        self.account_balance += amount
       
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        # return self

    def display_user_balance(self):
        print("User:",self.name,"Balance: $"+str(self.account_balance))
        # return self

    # def  transfer_money(self, other_user_account_ID, amount):
    #     self.transferList[other_user_account_ID] = amount
    #     self.account_balance -= amount
    #     return self


turki = User("Turki", "abcde@gmail.com", 90)

turki.display_user_balance()
