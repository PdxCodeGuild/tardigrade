

usr_grade = int(input('Please type in a grade 0-100: '))

if usr_grade in range(97, 101):     
    print('You got an A+!')
elif usr_grade in range(94, 97):     
    print('You got an A!')
elif usr_grade in range(90, 94):     
    print('You got an A-!')
elif usr_grade in range(87, 90):
    print('You got a B+.')
elif usr_grade in range(84, 87):     
    print('You got an B!')
elif usr_grade in range(80, 84):     
    print('You got an B-!')
# elif usr_grade in range(70, 80):
#     print('You got a C.')
elif usr_grade in range(77, 80):
    print('You got a C+.')
elif usr_grade in range(74, 77):     
    print('You got an C!')
elif usr_grade in range(70, 74):     
    print('You got an C-!')
# elif usr_grade in range(60, 70):
#     print('You got a D.')
elif usr_grade in range(67, 70):
    print('You got a D+.')
elif usr_grade in range(64, 67):     
    print('You got an D!')
elif usr_grade in range(60, 64):     
    print('You got an D-!')
else:
    print('You really NEED to study, F.')
