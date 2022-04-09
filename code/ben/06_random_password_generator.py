import string
import random

lower = (string.ascii_lowercase)
upper = (string.ascii_uppercase)
numbers = (string.digits)
spx = ("!@#$%^&*()''?><`~/-;:.")
while True:

    lowercase = int(input("Enter Desired Number of Lowercase Letters: "))
    uppercase = int(input("Enter Desired Number of Uppercase Letters: "))
    nums = int(input("Enter Desired Number of Numbers: "))
    special = int(input("Enter Desired Number of Special Characters: "))
    password = []
    for i in range(lowercase):
        password.append(random.choice(lower))
    for i in range(uppercase):
        password.append(random.choice(upper))
    for i in range(nums):
        password.append(random.choice(numbers))
    for i in range(special):
        password.append(random.choice(spx))
    random.shuffle(password)
    print("Your Password:" + " " + "".join(password))
    
    new_password = input("New Password? (y/n) ").lower()
    if new_password == "y":
        continue
    elif new_password == "n":
        break
    else:
        print("Invalid Response. Please Run Again")
        break