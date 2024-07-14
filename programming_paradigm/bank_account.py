class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance = amount + self.account_balance
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance = self.account_balance - amount
            return True

    def display_balance(self):
       return '$'+self.account_balance 