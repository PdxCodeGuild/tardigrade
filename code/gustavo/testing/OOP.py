


class bank_account:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(amount)
        return amount

    def withdrawal(self, rem_bal):
        self.balance -= rem_bal
        print(self.balance)
        return self.balance

    def bank_fees(self):
        self.balance -= self.balance * .05
        print(self.balance)
        return self.balance

    def display(self):
        
        message = f'Hello {self.name}, your account {self.accountnumber} has {self.balance} available.'
        return message
my_bank = bank_account(1000101, 'gus', 0)
my_bank.deposit(150)  
my_bank.withdrawal(25)
my_bank.bank_fees()
print(my_bank.display())

