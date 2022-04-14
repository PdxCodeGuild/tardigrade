import random

# num_1 = random.randrange(1,100)
# num_2 = random.randrange(1,100)
# num_3 = random.randrange(1,100)
# num_4 = random.randrange(1,100)
# num_5 = random.randrange(1,100)
# num_6 = random.randrange(1,100)

def pick6():
    balance = 0
    counter = 0
    exp = 0
    roi = 0
    while counter != 100000:
        counter += 1
        balance -= 2
        exp -= 2
        winner = [random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100)]
        ticket = [random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100), random.randrange(1,100)]
    
        set1 = set(winner)
        set2 = set(ticket)
        match = set1.intersection(set2)
        # print(match)
        if len(match) == 1:
            balance += 7
        elif len(match) == 2:
            balance += 100
        elif len(match) == 3:
            balance += 50000
        elif len(match) == 4:
            balance += 1000000
        elif len(match) == 6:
            balance += 25000000
            # print(len(match))
    roi = (balance - abs(exp))
    return f' Your balance is: ${balance}.00, Your ROI is ${roi}.00, You spent ${abs(exp)}.00'
    # return f'The winning numbers are: {winner} and your ticket is: {ticket}'
   
print(pick6())