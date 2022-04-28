# Bank Account Class
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a deposit() method which manages the deposit actions.
# Create a withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
import math


class Bank:
    def __init__(self, accountNum, name, balance):
        self.account_num = accountNum
        self.name = name
        self.balance = balance
    def deposit(self, money_in):
        return self.balance + money_in
        
    def withdrawl(self, money_out):
        return self.balance - money_out
        
    def bankFees(self, fees):
        fees = self.balance * .05
        return self.balance - fees
        
    def display(self, details):
        details = self.account_num, self.name, self.balance
        return details
       

chase = Bank(123456789, 'mike', 10)
print(chase.deposit(20))

chase = Bank(123456789, 'mike', 1000)
print(chase.withdrawl(465))

chase = Bank(123456789, 'mike', 5000)
print(chase.bankFees(5000))

chase = Bank(123456798, 'mike', 2230)
print(chase.display(1))


# this is a comment