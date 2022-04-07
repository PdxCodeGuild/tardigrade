

number_grade = input('Please enter your number grade: ')
number_grade = int(number_grade)


if number_grade <= 59:
    letter_grade = "F"
elif number_grade <= 69:
    letter_grade = "D"
elif number_grade <= 79:
    letter_grade = "C"
elif number_grade <= 89:
    letter_grade = "B"
else:
    letter_grade = "A"


mod_number = number_grade % 10





if number_grade == 100:
    letter_grade = "A+"

if number_grade >= 60 and number_grade != 100:
    if mod_number == 0 or mod_number <= 2:
        mod = '-'
    elif mod_number == 3 or mod_number <= 6:
        mod = ""
    elif mod_number == 7 or mod_number <= 9:
        mod = '+'

    print(letter_grade + mod)
else:
    print(letter_grade)
