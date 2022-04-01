

usr_grade = int(input('Please type in a grade 0-100: '))

if usr_grade in range(90, 101):     
    print('You got an A!')
elif usr_grade in range(80, 90):
    print('You got a B.')
elif usr_grade in range(70, 80):
    print('You got a C.')
elif usr_grade in range(60, 70):
    print('You got a D.')
else:
    print('You really NEED to study, F.')
