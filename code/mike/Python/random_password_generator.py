### Random Password Generator
###Part 1
###Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

i = 1
while 1:
    pw_length = int(input('Enter the length of your desired password: '))
    pw_num = int(input('Enter your desired number of passwords: '))
    for x in range(0, pw_num):
        new_password = " "
        for x in range(0, pw_length):
            characters = random.choice(chars)
            new_password = new_password + characters
        
        print("Password generated: ", new_password)