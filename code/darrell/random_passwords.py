# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters,
# e.g. a62xB95. Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string.
# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
pull_list = letters + digits + punctuation
# print(letters)
# print(digits)
# print(punctuation)
# print(pull_list)

n = input("Enter the desired password length (characters): ")
n = int(n)
counter = 0
password_list = []
while counter < n:
    r = random.choice(pull_list)
    password_list.append(r)
    counter += 1
password = "".join(password_list)

# print(password_list)
print(f"Your generated passsword is: {password}")


# # Part 2 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password.
# You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...).
# You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list)
# to shuffle it, and then ''.join(password_list) to turn it back into a string.

# import random
# import string

# letters = string.ascii_letters
# digits = string.digits
# punctuation = string.punctuation
# pull_list_lowercase = letters[:26].lower()
# pull_list_uppercase = letters[:26].upper()
# pull_list_numbers = digits
# pull_list_special = punctuation
# # print(pull_list_lowercase)
# # print(pull_list_uppercase)
# # print(pull_list_numbers)
# # print(pull_list_special)

# l = input("Enter the desired number of lowercase letters: ")
# u = input("Enter the desired number of uppercase letters: ")
# n = input("Enter the desired number of numbers: ")
# s = input("Enter the desired number of special characters: ")
# l = int(l)
# u = int(u)
# n = int(n)
# s = int(s)
# x = l+u+n+s
# print(f"Your password will be {x} characters long.")

# counter = 0
# password_list = []
# while counter < l:
#     rl = random.choice(pull_list_lowercase)
#     ru = random.choice(pull_list_uppercase)
#     rn = random.choice(pull_list_numbers)
#     rs = random.choice(pull_list_special)
#     password_list.append(rl)
#     password_list.append(ru)
#     password_list.append(rn)
#     password_list.append(rs)
#     counter += 1


# password = "".join(password_list)

# # print(password_list)
# print(f"Your generated password is: {password}")
