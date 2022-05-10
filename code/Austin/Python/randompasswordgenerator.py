def password_generator():
    import random 
    import string
    length = 0
    letters = string.ascii_letters 
    digits = string.digits
    punctuation = string.punctuation
    password = []

    letter_count = input("Enter how many letters you would like in your password:")
    l_count = int(letter_count)
    digit_count = input("Enter how many numbers you would like in your password:")
    d_count = int(digit_count)+int(letter_count)
    punctuation_count = input("Enter how many instances of punctuations you would like in your password:")
    p_count = int(punctuation_count)+int(digit_count)+int(letter_count)

    while l_count > length: 
        password.append(random.choice(letters))
        length +=1 
    while d_count > length: 
        password.append(random.choice(digits))
        length +=1 
    while p_count > length: 
        password.append(random.choice(punctuation))
        length +=1 
    else:
        random.shuffle(password)
        final_password = "".join(password)
        print(f"Your password is: {final_password}")
    
    generate = True
    while generate:
        new_password = input('Create a new password? Enter yes or no:')
        if new_password == 'yes':
            password_generator()
        else:
            break

password_generator()