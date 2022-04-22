class Bank:
    def __init__(self,account_number,name_first,name_last,balance):
        self.account_number = account_number
        self.fname = name_first
        self.lname = name_last
        self.balance = balance
            
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def user_information(self):
        print(self.deposit(20))


chase = Bank(1111,'Joshua','Pitter',10)
chase.deposit(20)
print(chase.balance)


