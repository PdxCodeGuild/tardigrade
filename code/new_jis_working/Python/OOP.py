#Bank Account Class
class Bank_Account:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def adding_money(self,deposited):
        self.balance += deposited
        return print(self.balance)
    
    def withdrawing_money(self, withdraw):
        self.balance -= withdraw
        return print(self.balance)

jis_account = Bank_Account(1720,"jis", 10000)
jis_account.adding_money(200)
jis_account.withdrawing_money(1)


