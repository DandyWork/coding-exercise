class BankAccount:
    def __init__(self, balance=0): #pas mangggil object BankAccount, auto create ini
        self.balance = balance #mulai dari 0

    def deposit(self, amount):
        # Setor duit
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        # Tarik duit
        if amount < 0:
            print("Withdraw amount must be positive")
        elif amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        # Show current balance
        return self.balance


# Example usage:
account = BankAccount(100)                 # Mulai dari 100
print("Balance:", account.get_balance())         
account.deposit(50)                        # +50 jadi 150
print("Balance:", account.get_balance())
account.deposit(-50)                       # Deposit harus positif, kasih "Deposit amount must be positive"
print("Balance:", account.get_balance())
account.withdraw(70)                       # -70 jadi 80
print("Balance:", account.get_balance())
account.withdraw(200)                      # balance gak cukup, → Kasih "Insufficient balance!"
print("Balance:", account.get_balance())   # Show balance

