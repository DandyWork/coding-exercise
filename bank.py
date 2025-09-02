class BankAccount:
    def __init__(self, balance=0):
        # This is the constructor. It sets the starting balance.
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        # Take money out of the account
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        # Show current balance
        return self.balance


# Example usage:
account = BankAccount(100)       # Start with balance = 100
account.deposit(50)              # Add 50 → balance becomes 150
account.deposit(-50)             # Negative amount -> print "Deposit amount must be positive"
account.withdraw(70)             # Subtract 70 → balance becomes 80
account.withdraw(200)            # Not enough → print "Insufficient balance!"
print("Final Balance:", account.get_balance())  # Show balance

