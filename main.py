from account import Account
from exceptions import InsufficientBalanceError
def Bank_account():
    print("=== Create your bank account ===")     
    owner_name = input("First name: ")
    try:
        balance = float(input("Balance: "))
    except ValueError:
        print("Invalid input. Setting initial balance to 0.0")
        balance = 0.0
    account = Account(owner_name, balance)
    print(f"Owner: {owner_name} | Balance: {balance}")
    print("--- Menu options: Enter 1 for Withdraw, 2 for Deposit, or 3 to Exit ---")
    return account
    
def handle_withdraw(account):
    try:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.") 
    except InsufficientBalanceError as e:
        print(e)
def deposit(account):
        try:
            amount = float(input("Enter amount to deposit:"))
            account.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
account=Bank_account()
while True:
     choice=input("\n1.Withdraw  2.Deposit  3.Exit\nChoose:")
     if choice == "1":
        handle_withdraw(account)
     elif choice == "2":
        deposit(account)
     elif choice =="3":
        print("Good bye")
        break
     else:
        print("invalid choice")