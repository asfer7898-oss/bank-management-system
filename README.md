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