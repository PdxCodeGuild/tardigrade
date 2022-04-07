#ask the user for their numerical score
score = input("Please enter your exam score: ")
score = float(score)
if score >= 97.5 and score <= 100:
    grade = "A+"
elif score >= 92.5 and score <= 97.4:
    grade = "A"
elif score >= 90 and score <= 92.4:
    grade = "A-"
elif score >=87.5 and score <90:
    grade = "B+"
elif score >= 82.5 and score <= 87.4:
    grade = "B"
elif score >= 80 and score <= 82.4:
    grade = "B-"
elif score >=77.5 and score <80:
    grade = "C+"
elif score >= 72.5 and score <= 77.4:
    grade = "C"
elif score >= 70 and score <= 72.4:
    grade = "C-"
elif score >=67.5 and score <70:
    grade = "D+"
elif score >= 62.5 and score <= 67.4:
    grade = "D"
elif score >= 60 and score <= 62.4:
    grade = "D-"
else:
    grade = "F"

print(f"Thank you. Your grade is {grade}")
