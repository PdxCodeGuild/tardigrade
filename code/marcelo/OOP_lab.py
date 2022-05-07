class BankAccount:
    def __init__(self, accountnum, name, balance):
        self.accountnum = accountnum
        self.name = name
        self.balance = balance
    
    def deposit(self):
        self.balance += new_deposit
        print(f'I have deposited {self.balance}')
        
    
    def withdrawl(self):
        self.balance -= new_withdrawl
        print(f'my balance after widthdrawl is {self.balance}')
    
    def bankfees(self):
        self.bankfee = self.balance * .05
        print(f'5% bank fee is {self.bankfee}')
    
    def display(self):
        self.final_balance = self.balance - self.bankfee 
        print(f'my total balance is {self.final_balance}')
  

marcelo= BankAccount('800800', 'aldo',1000)

new_deposit = 20000
new_withdrawl= 5000

print (marcelo.deposit(), marcelo.withdrawl(), marcelo.bankfees(), marcelo.display())