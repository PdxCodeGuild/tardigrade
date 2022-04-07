import random

def number_sec():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    user_number = 0

    while user_number < 3 or user_number > 5:
            user_number = int(input('How many numbers do you want in your password? You need at least 3 but no more than 5.\n'))
            if user_number >= 3 and user_number <= 5:
                continue
            else:
                print('You did not choose a satifactory number, Please try again\n\n')


    number_set = (random.sample(numbers, user_number))

    return number_set







   
    
    
def loLetter_sec():
    lo_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z'] 

    user_lo_letter = 0

    while user_lo_letter < 3 or user_lo_letter > 5:
        user_lo_letter = int(input('How many lower case letters do you want in your password? You need at least 3 but no more than 5.\n'))
        if user_lo_letter >= 3 and user_lo_letter <= 5:
            continue
        else:
            print('You did not choose a satifactory number, Please try again\n\n')
    
    loletter_set = (random.sample(lo_letter, user_lo_letter))

    return loletter_set


def upLetter_sec():
    up_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

    user_up_letter = 0

    while user_up_letter < 3 or user_up_letter > 5:
        user_up_letter = int(input('How many upper case letters do you want in your password? You need at least 3 but no more than 5.\n'))
        if user_up_letter >= 3 and user_up_letter <= 5:
            continue
        else:
            print('You did not choose a satifactory number, Please try again\n\n')

    
    upletter_set = (random.sample(up_letter, user_up_letter))
    
    return upletter_set
    
def symbol_sec():
    symbl = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

    user_symbl = 0

    while user_symbl < 3 or user_symbl > 5:
        user_symbl = int(input('How many symbols do you want in your password? You need at least 3 but no more than 5.\n'))
        if user_symbl >= 3 and user_symbl <= 5:
            continue
        else:
            print('You did not choose a satifactory number, Please try again\n\n')

    
    symbl_set = (random.sample(symbl, user_symbl))
    
    return symbl_set


def passwrd_combo(numbers,lower_letters ,upper_letters ,symbls):
    password_set = numbers + lower_letters + symbls + upper_letters
    random.shuffle(password_set)
    password_set = ''.join(password_set)
    print(f'Here is your password: {password_set}')







numbers = number_sec()
lower_letters = loLetter_sec()
upper_letters = upLetter_sec()
symbls = symbol_sec()
passwrd_combo(numbers,lower_letters ,upper_letters ,symbls)