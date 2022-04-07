import random
import string


abc= string.ascii_letters
numbers= string.digits
character= string.punctuation
secret= abc + numbers + character
password= ''
while len(password) < 10:
    password += random.choice(secret) 
print (f'your password: {password}')