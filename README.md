 # 🏦Bank Management System (Python OOP)

 A simple bank management system using Python OOP
---
## ✨Features
**Account Creation**: Interactive prompt to set up a new bank account with an owner name and initial balance.
- **Deposit Funds**: Securely deposit and withdraw funds with real-time balance checks.
- **Withdraw Funds**: Withdraw money with real-time balance verification.
- **Custom Exception Handling**: Uses a custom `InsufficientBalanceError` exception to handle over-withdrawals gracefully without crashing the application.
- **Modular Design**: Clean separation with `main.py` (user interface & control flow) and `account.py` (business logic & classes).
---
## 🛠️Project Structure
```text
bank-management-system/
│
├── main.py        # Main execution file containing the user interface, menu, and loops
├── account.py     # Contains the Account class and core banking logic
└── exceptions.py  # Contains custom exception classes (e.g., InsufficientBalanceError)
```
---
## 💻 Example Usage & Execution
```text
=== Create your bank account ===
First name: Asfer
Balance: 1000
Owner: Asfer | Balance: 1000.0
--- Menu options: Enter 1 for Withdraw, 2 for Deposit, or 3 to Exit ---

1.Withdraw  2.Deposit  3.Exit
Choose:1
Enter amount to withdraw: 100
withdraw:100.0|Your balance:900.0

1.Withdraw  2.Deposit  3.Exit
Choose:2
Enter amount to deposit:2000
Deposit: 2000.0 |Your balance:2900.0

1.Withdraw  2.Deposit  3.Exit
Choose:3
Good bye