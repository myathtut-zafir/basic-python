class Account():
    
    def __init__(self,owner,balance) -> None:
        self.owner=owner
        self.balance=balance

    def deposit(self,balance):
        self.balance+=balance
        print("Deposit accept")
    def withdraw(self,balance):
        if self.balance <= balance:
            return "u can't"
        else:
           self.balance= self.balance - balance
           return "success"

    def __str__(self):
        return "Account owner:  " + self.owner + "\nAccount balance: "+ str(self.balance)

acct1 = Account('Jose',100)
print(acct1)
print(acct1.balance)
print(acct1.deposit(100))
print(acct1.withdraw(200))
print(acct1.balance)
    