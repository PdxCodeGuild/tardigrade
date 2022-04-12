# Part 1

# Let's generate a password of length n using a while loop and random.choice, 
# this will be a string of random characters, e.g. a62xB95. 
# Allow the user to enter the value of n, 
# remember to convert its type to an int, as input returns a string.
#  Hint: random.choice can be used to pick a character out of a string, 
#  as well as an element out of a list.

import random
import string 

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_characters = letters + digits + punctuation

choices = []

n = input("How many characters would you like in your password? ")
n = int(n)

password_length = n
counter = 0
random_password = []

while counter < password_length:
    random_selection = random.choice(all_characters)
    random_password.append(random_selection)
    counter +=1

print("You're password is: " + "".join(random_password) + "\n")

# Part 2 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, 
# and special characters they'd like in their password. 
# You do not want the pieces in order 
# (e.g. 3 lowercase letters followed by 3 uppercase letters...). 
# You can use list(password_string) or password_string.split('') 
# to convert the string to a list, random.shuffle(password_list) to shuffle it, 
# and then ''.join(password_list) to turn it back into a string.

import random
import string 

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

choices = []

lowercase = input("For your password, please choose the number of...\n\nLOWERCASE LETTERS:    ")
uppercase = input("UPPERCASE LETTERS:    ")
numbers = input("NUMBERS:              ")
special_punctuation = input("SPECIAL PUNCTUATION:  ")

password_length = int(lowercase) + int(uppercase) + int(numbers) + int(special_punctuation)
counter = 0
random_password = []

while counter < password_length:
    for item in lowercase:
        random_selection = random.choice(letters).lower()
        random_password.append(random_selection)
        counter +=1
    for item in uppercase:
        random_selection = random.choice(letters).upper()
        random_password.append(random_selection)
        counter +=1
    for item in numbers:
        random_selection = random.choice(digits)
        random_password.append(random_selection)
        counter +=1
    for item in special_punctuation:
        random_selection = random.choice(punctuation)
        random_password.append(random_selection)
        counter +=1

random.shuffle(random_password)
print("\nYou're password is: " + "".join(random_password))
