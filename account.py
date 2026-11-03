from exceptions import InsufficientBalanceError

class Account:
    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient balance! Available: {self.balance}"
            )
        else:
            self.balance -= amount
            print(f"withdraw:{amount}|Your balance:{self.balance}")
    def deposit(self,amount):
        if amount<=0:
            print("Transaction failed !")
        else:
            self.balance +=amount
            print(f"Deposit: {amount} |Your balance:{self.balance}")