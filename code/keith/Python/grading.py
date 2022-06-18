
from pty import STDOUT_FILENO


student_grade = int(input("a number between 1 and 100: ")) 




if student_grade >= 90 and student_grade <= 94:
    print("A-")
elif student_grade >= 95 and student_grade <= 100:
    print("A+")    
elif student_grade >= 80 and student_grade <= 84:
    print("B-")
elif student_grade >= 85 and student_grade <= 89:
    print("B+")
elif student_grade >= 70 and student_grade <= 74:
    print("C-")
elif student_grade >= 75 and student_grade <= 79:
    print("C+") 
elif student_grade >= 60 and student_grade <=64:
    print("D-") 
elif student_grade >= 65 and student_grade <= 69:
    print("D+")
elif student_grade > 0 and student_grade <=59:
    print("F")           