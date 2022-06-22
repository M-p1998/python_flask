class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def display_user_balance(self):
        print("User: " + self.name + " , " "Balance: " +  str(self.account_balance) )
        return self
   
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
        
guido = User("Guido van Rossum")
guido.make_deposit(200).make_deposit(500).make_deposit(300).make_withdrawal(100).display_user_balance()

adrian = User('Adrian')
adrian = User("Adrian").make_deposit(100).make_deposit(300).make_withdrawal(50).make_withdrawal(100).display_user_balance()

jenny = User("Jenny")
jenny.make_deposit(500).make_withdrawal(100).make_withdrawal(200).make_withdrawal(50).display_user_balance()

guido.transfer_money(200,jenny)
