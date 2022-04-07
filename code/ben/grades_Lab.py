def grades(x):
    if grade >= 100:
        print('A+')
    elif grade >= 93:
        print('A')
    elif grade >= 90:
        print('A-')
    elif grade >= 88:
        print('B+')
    elif grade >= 83:
        print('B')
    elif grade >= 80:
        print('B-')
    elif grade >= 78:
        print('C+')
    elif grade >= 73:
        print('C')
    elif grade >= 70:
        print('C-')
    elif grade >= 68:
        print('D+')
    elif grade >= 63:
        print('D')
    elif grade >= 60:
        print('D-')
    else:
        print("F")

while True:   
    grade= int(input("Please enter your grade in numerical format: "))
    grades(grade)    
    enter_again = input("Continue? (y/n) ").lower()
    if enter_again == "y":
        continue
    elif enter_again == "n":
        break
    else:
        print("Invalid Response. Please Run Again")
        break