#PNC Bank
class Bank_Account:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, num):
        self.balance += num

    def withdrawal(self, num):
        self.balance -= num

    def bankFees(self):
        self.balance *= .95

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

Account_1 = Bank_Account('0001','John Chapman', 25)
Account_2 = Bank_Account('0002', 'Susie Q', 1000)
Account_3 = Bank_Account('0003', 'Micheal Scott', 25)

Account_1.display()
Account_1.deposit(2500)
Account_1.bankFees()
Account_2.withdrawal(50.00)
Account_2.display()