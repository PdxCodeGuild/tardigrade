score = int(input('Enter a score between 0-100:'))

if score >= 90:
    grade = ['A']
elif 89 >= score >= 80:
    grade = ['B']
elif 79 >= score >= 70:
    grade = ['C']
elif 69 >= score >= 60:
    grade = ['D']
elif 59 >= score >= 0:
    grade = ['F']

modifier = list(str(score))
modifier.reverse()

if len(modifier) == 1:
    modifier.append("0")
elif int(modifier[1]) == 0 or int(modifier[0]) > 6:
    grade.append("+")
elif int(modifier[0]) < 4 and int(modifier[2]) != 0:
    grade.append("-")
else:
    pass

if grade[0] == 'F':
    grade.pop(1)
else: 
    pass

print("".join(grade))