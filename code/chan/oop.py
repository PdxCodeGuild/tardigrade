# Chan Saechao
# Object Oriented Programming

class bank_account:

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def bankFees(self): 
        print("# ----------------------------------------------------------------------------------- #")
        self.after_fee = self.balance * .95
        self.fee = self.balance - self.after_fee
        print('Bank Fee: ', self.fee)
        self.balance -= self.fee
        print('After bank fee: ', self.balance)

    def deposit(self, deposit_money):
        print("# ----------------------------------------------------------------------------------- #")
        self.balance += deposit_money
        print("Deposit: ", deposit_money)
        print("Remaining Balance: ", self.balance)

    def withdrawl(self, withdrawl_money):
        print("# ----------------------------------------------------------------------------------- #")
        self.balance -= withdrawl_money
        print("Withdrawl: ", withdrawl_money)
        print("Remaining Balance: ", self.balance)

    def display(self):
        print("# ----------------------------------------------------------------------------------- #")
        print(f"Account: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("# ----------------------------------------------------------------------------------- #")

my_bank_account = bank_account(987654321, 'Chan Saechao', 10000)
my_bank_account.bankFees()
my_bank_account.deposit(1700)
my_bank_account.withdrawl(700)
my_bank_account.display()
    
class rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width
        self.display()

    def perimeter(self):
        rectangle_perimeter = self.length * 2 + self.width * 2
        print(f"Perimeter: {rectangle_perimeter} ft")

    def area(self):
        rectangle_area = self.length * self.width
        print(f"Area: {rectangle_area} ft^2")

    def display(self):
        print(f"Length: {self.length} ft")
        print(f"Width: {self.width} ft")
        self.perimeter()
        self.area()

# Separator line
print("# ----------------------------------------------------------------------------------- #")

class parallelepiped(rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        self.volume()

    def volume(self):
        # I am pretty sure the volume for a parallelepiped formula is wrong
        self.rectangle_volume = self.length * self.width * self.height
        print(f"Volume: {self.rectangle_volume} ft^3")

volume_object = parallelepiped(4, 6, 4)

class person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)
        self.display()

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class student(person):
    def __init__ (self, name, age, school):
        super().__init__(name, age)
        self.school = str(school)
        self.displayStudent()
 
    def displayStudent(self):
        print(f"School: {self.school}")

me = student("Chan Saechao", "34", "PDX Code Guild")