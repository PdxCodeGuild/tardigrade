# Chan Saechao
# Grading

# Let's convert a number grade to a letter grade, using if and elif statements and comparisons. 
# First have the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.

# Ask for a grade from the user
grade_input = input("Please enter a grade: ")
grade_input = int(grade_input)
grade = 'NA'

# Grade function
def grade(score):
    # Made the grade for each Grade 2 elif because I didn't want the lines to get too long
    # grade 90-100: A
    grade_input = score
    if grade_input == 100 or grade_input == 99 or grade_input == 98 or grade_input == 97 or grade_input == 96:
        return 'A'
    elif grade_input == 95 or grade_input == 94 or grade_input == 93 or grade_input == 92 or grade_input == 91 or grade_input == 90:
        return 'A'
    # grade 80-89: B
    elif grade_input == 89  or grade_input == 88 or grade_input == 87 or grade_input == 86 or grade_input == 85:
        return 'B'
    elif grade_input == 84 or grade_input == 83 or grade_input ==  82 or grade_input == 81 or grade_input == 80:
        return 'B'
    # grade 70-79: C
    elif grade_input == 79 or grade_input == 78 or grade_input == 77 or grade_input == 76 or grade_input == 75:
        return 'C'
    elif grade_input == 74 or grade_input == 73 or grade_input == 72 or grade_input == 71 or grade_input == 70:
        return 'C'
    # grade 60-69: D
    elif grade_input == 69  or grade_input == 68 or grade_input == 67 or grade_input == 66 or grade_input == 65:
        return 'D'
    elif grade_input == 64 or grade_input == 63 or grade_input == 62 or grade_input == 61 or grade_input == 60:
        return 'D'
    # grade 0-59: F
    else:
        return 'F'

# Store your grade and score to reuse the if statement
your_score = grade_input
your_grade = grade(your_score)

# Function for grade + - or normal grade
def  grade_rate(score):
    grade = score % 10
    if grade == 5:
        return ''
    elif grade == 1 or grade == 2 or grade == 3 or grade == 4:
        return '-'
    else: 
        return '+'

# Get your grade degree as in + - or normal
your_grade_plus= grade_rate(your_score)
# print(f'Your grade degree:{your_grade_plus}')

# Print scores and grade 
print(f'''Your score is  {your_score}.
Your grade is {your_grade}{your_grade_plus}.''')