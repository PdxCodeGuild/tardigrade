

grade = input("Please enter a grade: " )
grade = float(grade)

if grade >= 90:
    if grade%10 >= 5:
        print("A+")
    else:
        print("A-")
elif grade <= 89 and grade >= 80:
    if grade%10 >= 5:
        print("B+")
    else:
        print("B-")
elif grade <= 79 and grade >= 70:
    if grade%10 >= 5:
        print("C+")
    else:
        print("C-")
elif grade <= 69 and grade >=60:
    if grade%10 >= 5:
        print("D+")
    else:
        print("D-")
if grade <= 59:
    if grade%10 >= 5:
        print("F+")
    else:
        print("F-")
