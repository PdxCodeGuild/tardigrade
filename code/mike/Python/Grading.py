### Part 1

student_grade = input('Enter your score to receive your grade:')
student_grade = (int(student_grade))
print(type(student_grade))
if student_grade >= 90 and student_grade <= 100:
    print('A')


elif student_grade >= 80 and student_grade <= 89:
    print('B')

elif student_grade >= 70 and student_grade <= 79:
    print('C')

elif student_grade >= 60 and student_grade <= 69:
    print('D')

elif student_grade > 0 and student_grade <= 59:
    print('F')

print('testing with Alex')

### Part 2

student_grade = input('Enter your score to receive your grade:')
student_grade = (int(student_grade))
print(type(student_grade))
if student_grade >= 90 and student_grade <= 93:
    print('A-')

elif student_grade >= 94 and student_grade <= 96:
    print('A')

elif student_grade >= 97 and student_grade <= 100:
    print('A+')

elif student_grade >= 80 and student_grade <= 83:
    print('B-')

elif student_grade >= 84 and student_grade <= 86:
    print('B')

elif student_grade >= 87 and student_grade <= 89:
    print('B+')

elif student_grade >= 70 and student_grade <= 73:
    print('C-')

elif student_grade >= 74 and student_grade <= 76:
    print('C')

elif student_grade >= 77 and student_grade <= 79:
    print('C+')

elif student_grade >= 60 and student_grade <= 63:
    print('D-')

elif student_grade >= 64 and student_grade <= 66:
    print('D')

elif student_grade >= 67 and student_grade <= 69:
    print('D+')

elif student_grade > 0 and student_grade <= 53:
    print('F-')

elif student_grade > 54 and student_grade <= 56:
    print('F')

elif student_grade > 57 and student_grade <= 59:
   print('F')
