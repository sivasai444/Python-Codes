class Account:
    def _init_(self, balance):
        self.balance = balance
        self.min_balance = 0

    def withdraw(self, amount):
        if ((self.balance - amount) >= self.min_balance):  # Fill in Blank1 and Blank2 here
            return amount
        else:
            return 0

class SavingsAccount(Account):
    def _init_(self, balance):
        super()._init_(balance)
        self.min_balance = 500

class CurrentAccount(Account):
    def _init_(self, balance):
        super()._init_(balance)
        self.min_balance = 0

a1 = SavingsAccount(1000)
a2 = CurrentAccount(1000)
accounts = [a1, a2]
for account in accounts:
    print(account.withdraw(1000))
