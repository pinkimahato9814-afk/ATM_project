
class BankAccount:
    def __init__(self, account_number=12345, balance=50000):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"""
 DEPOSIT SUCCESSFUL
DEPOSITED AMOUNT :: {amount}
TOTAL BALANCE AFTER DEPOSIT :: {self.balance}
"""

    def withdraw(self, amount):
        if amount > self.balance:
            return f"""
 WITHDRAWAL FAILED
INSUFFICIENT BALANCE
CURRENT BALANCE :: {self.balance}
"""
        else:
            self.balance -= amount
            return f"""
 WITHDRAWAL SUCCESSFUL
WITHDRAWN AMOUNT :: {amount}
TOTAL BALANCE AFTER WITHDRAWAL :: {self.balance}
"""

    def get_balance(self):
        return f"""
 YOUR CURRENT BALANCE IS :: {self.balance}
"""


class SavingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_earned = 0

    def add_interest(self):
        interest_rate = 5  # 5%
        earned_interest = self.balance * (interest_rate / 100)

        self.balance += earned_interest
        self.interest_earned += earned_interest

        return f"""
 INTEREST ADDED SUCCESSFULLY
INTEREST RATE :: {interest_rate}%
INTEREST AMOUNT :: {earned_interest}
TOTAL INTEREST EARNED SO FAR :: {self.interest_earned}
TOTAL BALANCE AFTER ADDING INTEREST :: {self.balance}
"""


# Create Account
instance = SavingAccount()

# Main Program Loop
while True:

    print("""
=========  WELCOME TO WORLD BANK =========

Choose an option:
D :: DEPOSIT
W :: WITHDRAW
G :: GET BALANCE
I :: ADD INTEREST
E :: EXIT
""")

    mode = input("Enter your choice: ").upper()
    output = ""

    match mode:

        case "D":
            try:
                deposit_amt = float(input("Enter deposit amount: "))
                if deposit_amt <= 0:
                    output = " Please enter a valid positive amount!"
                else:
                    output = instance.deposit(deposit_amt)
            except ValueError:
                output = " Invalid input! Please enter numbers only."

        case "W":
            try:
                withdrawal_amount = float(input("Enter withdrawal amount: "))
                if withdrawal_amount <= 0:
                    output = " Please enter a valid positive amount!"
                else:
                    output = instance.withdraw(withdrawal_amount)
            except ValueError:
                output = " Invalid input! Please enter numbers only."

        case "G":
            output = instance.get_balance()

        case "I":
            output = instance.add_interest()

        case "E":
            print(" Thank you for banking with us!")
            break

        case _:
            output = " Invalid option selected!"

    print(output)
