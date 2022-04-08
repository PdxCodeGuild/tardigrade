import string
import random
pass_list =[]
# pass_str = ''
pass_len = input('Please enter the length of the password: ')
while len(pass_list) < int(pass_len):
    pass_list.append(random.choice(string.digits))
    pass_list.append(random.choice(string.ascii_letters))
    pass_list.append(random.choice(string.punctuation))
    random.shuffle(pass_list)
    pass_str = ''.join(pass_list)
print(pass_str)

