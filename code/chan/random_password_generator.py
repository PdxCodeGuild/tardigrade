# Chan Saechao
# Random Password Generator
import string
import random

"""
Part 1

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. 
Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string. Hint: random.choice can be used 
to pick a character out of a string, as well as an element out of a list.

Part 2

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. You do not 
want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You can use list(password_string) or
password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.
"""

def random_password_generator(lower_case, upper_case, number_input, special_characters):
    generated_password = ""
    lower_case_amount = 0
    upper_case_amount = 0
    number_amount =  0
    special_characters_amount = 0

    # String list from import string
    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    number_list =  list(string.digits)
    special_list = list(string.punctuation)
    # print(number)

    # Len of string
    lower_len = len(lower_list)
    upper_len  = len(upper_list)
    number_len = len(number_list)
    special_len = len(special_list)
    # print(lower_len)
    # print(upper_len)
    # print(number_len)
    # print(special_len)

    # Pass for lower/upper/special
    lower_pass = ''
    upper_pass = ''
    number_pass = ''
    special_pass = ''
    combined_pass = ''

    while lower_case_amount < lower_case:
        # Gets random number in range of len of lower_case string
        random_num =  random.randint(0, lower_len - 1)
        # print(f'my random num: {random_num}')
        # Use the random number to get the list index character and add it into the password string for lower case
        lower_pass += lower_list[random_num]
        # print(lower_case)
        # print(lower_pass)
        lower_case_amount += 1

    while upper_case_amount < upper_case:
        # Gets random number in range of len of upper_case string
        random_num =  random.randint(0, upper_len - 1)
        # print(f'my random num: {random_num}')
        # Use the random number to get the list index character and add it into the password string for upper case
        upper_pass += upper_list[random_num]
        # print(upper_case)
        # print(upper_pass)
        upper_case_amount +=  1

    while number_amount < number_input:
        # Gets random number in range of len of upper_case string
        random_num =  random.randint(0, number_len - 1)
        # print(f'my random num: {random_num}')
        # Use the random number to get the list index character and add it into the password string for number
        number_pass += number_list[random_num]
        # print(upper_case)
        # print(upper_pass)
        number_amount +=  1

    while special_characters_amount < special_characters:
        # Gets random number in range of len of special_case string
        random_num =  random.randint(0, special_len - 1)
        # print(f'my random num: {random_num}')
        # Use the random number to get the list index character and add it into the password string for special 
        special_pass += special_list[random_num]
        # print(special_characters)
        # print(special_pass)
        special_characters_amount += 1

    combined_pass = lower_pass + upper_pass + number_pass + special_pass
    # print(f'combined pass: {combined_pass}')
    # Change into list
    combined_pass_list = list(combined_pass)
    # print(f'combined list {combined_pass_list}')
    random.shuffle(combined_pass_list)
    # print(f'combined list sorted: {combined_pass_list}')
    generated_password = ''.join(combined_pass_list)
    print(f'Your generated pass is: {generated_password}')

print('Random Password Generator')
lower_char = int(input("How many lower case characters in  your password? " )) 
upper_char = int(input("How many upper case characters in  your password? " )) 
number_char = int(input("How many number characters in  your password?" )) 
special_char = int(input("How many speciale characters in  your password? " )) 
random_password_generator(lower_char,upper_char,number_char,special_char)