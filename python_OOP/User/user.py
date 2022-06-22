class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_withdrawal(self,amount):
        self.account_balance -= amount
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def display_user_balance(self):
        print("User: " + self.name + " , " "Balance: " +  str(self.account_balance) )
   
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        
guido = User("Guido van Rossum")
guido.make_deposit(200)
guido.make_deposit(500)
guido.make_deposit(300)
guido.make_withdrawal(100)
guido.display_user_balance()
adrian = User("Adrian")
adrian.make_deposit(100)
adrian.make_deposit(300)
adrian.make_withdrawal(50)
adrian.make_withdrawal(100)
adrian.display_user_balance()
jenny = User("Jenny")
jenny.make_deposit(500)
jenny.make_withdrawal(100)
jenny.make_withdrawal(200)
jenny.make_withdrawal(50)
jenny.display_user_balance()

guido.transfer_money(200,jenny)

#  #


