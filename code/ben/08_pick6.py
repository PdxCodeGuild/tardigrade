import string
import random

def pick6():
    numbers = list(range(1,100))
    pick_list = []
    for i in range(0,6):
        pick_list.append(random.choice(numbers))
    return (pick_list)

def tix6():
    numbers = list(range(1,100))
    tix_list = []
    for i in range(0,6):
        tix_list.append(random.choice(numbers))
    return (tix_list)

def match_list(x,y):
    matched_list = []
    for i in range(len(x)):
        if i in range(len(y)):
            if x[i] == y[i]:
                matched_list.append(i)
    return [x[i] for i in matched_list]

print("Pick6 Game")
number = 10
total_balance = 0
for x in range(number):
    balance = 0
    picks = pick6()
    print(f"Your picks:{picks}")
    tix = tix6()
    print(f"The winning numbers: {tix}")
    matches = match_list(picks,tix)
    print(f" Here are the matches(if any): {matches}")
    count = 0
    for match in matches:
        count +=1
    print(f"Here is how many you matched: {count}")
    if count == 1:
        balance += 4
    elif count == 2:
        balance += 7
    elif count == 3:
        balance += 100
    elif count == 4:
        balance += 50000
    elif count == 5:
        balance += 1000000
    elif count == 6:
        balance += 25000000
    else:
        balance += 0
    new_balance = balance - 2
    total_balance = total_balance + new_balance
    
expenses = number * 2
roi = (balance - expenses) / expenses

finish = f"""
Your total balance after {number} games is ${total_balance}.00.
Your total expenses were: ${expenses}.
Your earnings are: ${balance}.
Your ROI is: ${roi}.
"""
print(finish)