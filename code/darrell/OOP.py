class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            return ("not enough money")
        else:
            self.balance -= amount
            return self.bank_fees()

    def bank_fees(self):
        self.balance -= self.balance * .05
        return self.balance

    def display(self):
        display_acct = [self.accountNumber, self.name, self.balance]
        print(display_acct)
        return display_acct

    def check_balance(self):
        return f"Your balance is ${self.balance}"


wells_fargo = BankAccount(34003402, "darrell eikner", 400)
print(wells_fargo.deposit(25))


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def area(self):
        area = self.length * self.width
        return area

    def display(self):
        display_list = [self.length, self.width, self.perimeter, self.area]
        print(display_list)
        return display_list


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        vol = self.length * self.width * self.height
        return vol


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        display_person = [self.name, self.age]
        print(display_person)
        return display_person


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        display_student = [self.name, self.age, self.section]
        print(display_student)
        return display_student
