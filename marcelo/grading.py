grade= input(' enter a grade you got from your fake test today: ')
grade = int(grade)

if grade >= 95:
    print('you got A+')
elif grade >= 90:
    print('you got A-')
elif grade >= 85:
    print('you got B+')
elif grade >= 80:
    print('you got B-')
elif grade >= 75:
    print('you got C+')
elif grade >= 70:
    print('you got C-')
elif grade >= 60:
    print('you got D')
elif grade < 59:
    print('you got F')

