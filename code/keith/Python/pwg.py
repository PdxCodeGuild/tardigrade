from ast import Num
import random
# these next lines list all my possible characters to be generated 
# and combines them to into one variable
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
integers = "0123456789"
chars = "~!@#$%^&*?()_+}{|"
all_chars = uppercase_letters + lowercase_letters + integers + chars
# this line makes my password a list
password = []
#this line makes the length of my final password generated only ten characters
while len(password) < 10:
     password.append(random.choice(all_chars))
answer = ""
# this next line converts the data type to list as a string without the commas
for char in password:
    answer = char + answer
print('Your password is: ' + answer)
