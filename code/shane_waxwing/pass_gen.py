import random

upper_string = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_string = "qwertyuiopasdfghjklzxcvbnm"
char_string = "!@#$%^&*()_+|}{:?><,./;[]\=-"
number_string = "1029384756"
all_char = "QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+|}{:?><,./;[]\=-qwertyuiopasdfghjklzxcvbnm1029384756"

password_list = []
password = ""

n = input("Enter a number for the length of your password: ")
 
while len(password_list) < int(n):
    password_list.append(random.choice(all_char))

print(password.join(password_list))
