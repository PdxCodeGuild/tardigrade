class BankAccount:
        def __init__(self, accountNumber, name, balance):
            self.accountNumber = accountNumber
            self.name = name
            self.balance = balance
        def deposit(self,num):
            self.balance = self.balance + num
        def withdraw(self,num):
            self.balance = self.balance - num
        def bankFees(self):
            self.balance = self.balance - (self.balance *0.05)
        def display(self):
            print("Account number: " + str(self.accountNumber))
            print("Account holder: " + self.name)
            print("Final account balance: " +str(self.balance))
a = BankAccount(70051901, "Alex", 4000)
a.deposit(2000)
a.withdraw(1000)
a.bankFees()
a.display()

class Rectangle:
        def __init__(self, length, width, perimeter, area):
            self.length = length
            self.width = width
            self.perimeter = perimeter
            self.area = area
        def Perimeter(self):
            self.perimeter = self.length + self.length + self.width + self.width
        def Area(self):
            self.area = self.length * self.width
            
class Parallelepipede(Rectangle):
    def __init__(self, length, width, perimeter, area, height, volume):
        self.height = height
        self.volume = volume
        
        super().__init__(length, width, perimeter, area)
        
    def Volume(self):
        self.volume = self.length * self.width * self.height
        
    def display(self):
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))
        print("Perimeter: " + str(self.perimeter))
        print("Area: " + str(self.area))
        print("Height: " + str(self.height))
        print("Volume: " + str(self.volume))
            
a = Parallelepipede(10,8,0,0,5,0)
a.Perimeter()
a.Area()
a.Volume()
a.display()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:" + self.name)
        print("Age: " + str(self.age))
        
class Student(Person):
    def __init__(self, name, age, section):
        self.section = section
        
        super().__init__(name, age)
        
    def displayStudent(self):
        print("Student Info: " + self.name + "," + " " + str(self.age) + "," + " " + "Section: " + self.section)
        
a = Student('Alex', 32, "Python")
a.display()
a.displayStudent()