# 📌 Problem: Implement a BankAccount Class
# Create a class that represents a simple bank account with the following functionality:
# - Store account number, account holder's name, and balance.
# - Deposit money into the account.
# - Withdraw money from the account (only if sufficient balance is available).
# - Display the current balance.

# 🧠 Approach:
# - Define a class `BankAccount` with attributes: `acc_no`, `acc_holder_name`, and `balance`.
# - Implement a method `deposit_money(amount)` that increases the balance if the amount > 0,
#   otherwise print an error message.
# - Implement a method `withdraw_money(amount)` that decreases the balance if amount > 0
#   and less than or equal to current balance, otherwise print an error message.
# - Implement a method `display_info()` that prints the current balance.
# - Create an object of the class and test deposit, withdrawal, and display functionality.

class BankAccount:
    def __init__(self,acc_no,acc_holder_name,balance):
        self.acc_no = acc_no
        self.acc_holder_name = acc_holder_name
        self.balance = balance
    def deposit_money(self,amount):
        if amount>0:
            self.balance+=amount
            print("Amount successfully deposited")
            print(f"New balance:{self.balance}")
        else:
            print("Cannot add negative or 0 money")
    def withdraw_money(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print("Amount withdrawn")
            print(f"New balance:{self.balance}")
        elif amount<0:
            print("Cannot withdraw negative money")
        else:
            print("Insufficient amount")
    def display_info(self):
        print(f"Current balance:{self.balance}")

p1 = BankAccount(234,"Tirth",5000)
p1.deposit_money(1000)
p1.withdraw_money(2000)
p1.display_info()

