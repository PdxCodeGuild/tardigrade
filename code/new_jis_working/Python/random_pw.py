
import random
import string


all_characters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)


#print(all_characters)

n = int(input("How long would you like your pw to be?: "))
password = []

while len(password) < n:
    password.append(random.choice(all_characters))


password = ''.join(password)
print(f' Your generated password is: {password}')