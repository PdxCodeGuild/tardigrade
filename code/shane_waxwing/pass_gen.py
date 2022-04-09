# import random

# upper_string = "QWERTYUIOPASDFGHJKLZXCVBNM"
# lower_string = "qwertyuiopasdfghjklzxcvbnm"
# char_string = "!@#$%^&*()_+|}{:?><,./;[]\=-"
# number_string = "1029384756"
# all_char = "QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+|}{:?><,./;[]\=-qwertyuiopasdfghjklzxcvbnm1029384756"

# password_list = []
# password = ""

# n = input("Enter a number for the length of your password: ")
 
# while len(password_list) < int(n):
#     password_list.append(random.choice(all_char))

# print(password.join(password_list))


import random

upper_string = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_string = "qwertyuiopasdfghjklzxcvbnm"
char_string = "!@#$%^&*()_+|}{:?><,./;[]\=-"
number_string = "1029384756"

pass_list = []


#_______________________________ generating list of user designated number of charicters__________________________________#

upper_seg = int(input("Enter number of upper case letters: "))
for number in range(upper_seg):
    pass_list.append(random.choice(upper_string))

lower_seg = int(input("Enter number of lower case letters: "))
for number in range(lower_seg):
    pass_list.append(random.choice(lower_string))

spec_char_seg = int(input("Enter number of special charicters: "))
for number in range(spec_char_seg):
    pass_list.append(random.choice(char_string))

num_seg = int(input("Enter number of numbers: "))
for number in range(num_seg):
    pass_list.append(random.choice(number_string))

#___________________________________________________________________________________________________________________________#

random.shuffle(pass_list)
print("".join(pass_list))
