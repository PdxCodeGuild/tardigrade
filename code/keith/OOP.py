# Lab: Object Oriented Programming
# Bank Account Class
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a deposit() method which manages the deposit actions.
# Create a withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
# Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another volume() method to calculate the volume of the Parallelepiped.
# Person Class
# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.



from types import new_class



class Bank_account():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdrawal(self, taken):
        if taken > self.balance:
            print('NOT ENOUGH MONEY')
        else:
          self.balance -= taken
          return self.balance
    
    def check_balance(self):
        return f"your balance is {self.balance}"
    
    def bankfees(self):
        self.balance = self.balance - self.balance * .05
        return self.balance

    def display(self):
        account_details = f"Your balance after depositing is: {self.balance}    "
        print(account_details)


wells_fargo = Bank_account("12345", 'Keith', 91)
print(wells_fargo.deposit(10))
print(wells_fargo.withdrawal(0))
print(wells_fargo.bankfees())
print(wells_fargo.display())