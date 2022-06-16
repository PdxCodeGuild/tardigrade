## NOTES - Follow-up to second quarter progress report
#
# Eberhardt

## https://github.com/PdxCodeGuild/hydra/blob/master/1%20Python/labs/OOP.md

## Lab 1 - COMPLETE

## Bank Account Class
## -Create a Python class called BankAccount which represents a bank account,
## having as attributes: accountNumber (numeric type), name (name of the account owner
## as string type), balance.
## -Create a constructor with parameters: accountNumber, name, balance.
## -Create a deposit() method which manages the deposit actions.
## -Create a withdrawal() method which manages withdrawals actions.
## -Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
## -Create a display() method to display account details.


class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self):
        print(
            f"Thank you {self.name} for choosing to 'Deposit' funds to account number {self.accountNumber}."
        )
        deposit = int(input(f"How much $$$ would you like to deposit? "))
        self.balance += deposit
        print(f"Deposit complete! Yout available funds are now ${self.balance}\n")

    ## Alex's Example
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self):
        print(
            f"Thank you {self.name} for choosing to 'Withdrawal' funds from account number {self.accountNumber}."
        )
        withdrawal = int(input(f"How much $$$ would you like to withdrawal? "))
        self.balance -= withdrawal
        print(f"Withdrawal complete! Yout available funds are now ${self.balance}\n")

    ## Alex's Example
    def withdrawal(self, amount):
        self.balance -= amount
        return self.balance

    def bankFees(self):
        bankFees = (self.balance * 0.05) + self.balance
        print(
            f"""\nThank you {self.name} for choosing to bank with 'Hardt Banking'.
To continue providing optimal service, a small banking fee will be applied to your account.
The total charge will be 5% of the valance on account #{self.accountNumber}, or, ${bankFees} in total.
If you have any questions regarding the impending charge, please contact customer service at:
☎️  1-800-YUR-EFFD
"""
        )

    def display(self):
        print(
            f"""
========ACCOUNT DETAILS========
              👤
          NAME: {self.name}
ACCOUNT NUMBER: {self.accountNumber}
       BALANCE: {self.balance}   
        """
        )


Christian = BankAccount(12345678, "Christian Eberhardt", 50000)
Nancy = BankAccount(98765432, "Nancy EBerhardt", 100000)

## TEST STATEMENTS

Christian.deposit()
Christian.withdrawal()
Christian.bankFees()
Christian.display()

print(Christian.withdrawal(10))
print(Christian.deposit(100))


## Lab 2 - COMPLETE
## Rectangle Class
## -Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
## -Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the
## area of ​​the rectangle.
## -Create a method display() that display the length, width, perimeter and area of an object created using an
## instantiation on rectangle class.
## -Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another
## volume() method to calculate the volume of the Parallelepiped. ## WHAT????


class Rectangle:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        print(f"The perimeter of the {self.name} is {perimeter} units.\n")

    def area(self):
        area = self.length * self.width
        print(f"The area of the {self.name} is {area} units.\n")

    def display(self):
        print(
            f"The length of the area is {self.length} while the width is {self.width}. Therefore: \n"
        )
        self.perimeter()
        self.area()


class Parallelepipede(Rectangle):
    def __init__(self, name, length, width, height):
        super().__init__(name, length, width)
        self.height = height

    def volume(self):
        volume = self.length * self.width * self.height
        print(f"The volume of the {self.name} is {volume} units.")


area1 = Rectangle("yard", 20, 30)
area2 = Rectangle("bedroom", 10, 10)
area3 = Parallelepipede("pool", 40, 80, 12)

## TEST STATEMENTS

area1.perimeter()
area2.perimeter()

area1.area()
area2.area()

area1.display()
area2.display()

area3.volume()

# ## Lab 3 - COMPLETE
# Person Class
# -Create a Python class Person with attributes: name and age of type string.
# -Create a display() method that displays the name and age of an object created via the Person class.
# -Create a child class Student which inherits from the Person class and which also has a section attribute.
# -Create a method displayStudent() that displays the name, age and section of an object created via the Student class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)

    def display(self):
        print(
            f"""
   Name: {self.name}
    Age: {self.age}"""
        )


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(
            f"""
   Name: {self.name}
    Age: {self.age}   
Section: {self.section}
"""
        )


person1 = Person("Donahue", 45)
person2 = Student("William", 16, "B")

## TEST STATEMENTS

person1.display()
person2.displayStudent()
