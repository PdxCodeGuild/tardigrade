# Let's convert a number to a letter grade, using if and elif statements and comparisons. 
# First have the user enter a number representing the grade (0-100). 
# Then convert the number grade to a letter grade.

# Numeric Ranges:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

numeric_grade = input("Please enter your grade as a percentile (0-100): ")
numeric_grade = int(numeric_grade)

achievement = (numeric_grade%10)

if numeric_grade >= 90 and numeric_grade <= 100:
    letter_grade = 'A'
    if achievement == 0 or achievement == 8 or achievement ==9:
        value = '+'
    elif achievement >= 0 and achievement <= 2:
        value = '-'
elif numeric_grade >= 80 and numeric_grade <= 89:
    letter_grade = 'B' 
    if achievement >= 7 and achievement <= 9:
        value = '+'
    elif achievement >= 0 and achievement <= 2:
        value = '-'
elif numeric_grade >= 70 and numeric_grade <= 79:
    letter_grade = 'C'
    if achievement >= 7 and achievement <= 9:
        value = '+'
    elif achievement >= 0 and achievement <= 2:
        value = '-'
elif numeric_grade >= 60 and numeric_grade <= 69:
    letter_grade = 'D'
    if achievement >= 7 and achievement <= 9:
        value = '+'
    elif achievement >= 0 and achievement <= 2:
        value = '-'
elif numeric_grade >= 0 and numeric_grade <= 59:
    letter_grade = 'F'
    value = ''

print(f"\nYour percentile of {numeric_grade} means you've earned a {letter_grade}{value}.\n")
