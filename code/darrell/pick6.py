import random

winning = []


def pick6():

    for i in range(6):
        random_num = random.randint(1, 99)
        winning.append(random_num)
    print(f"Winning Numbers: {winning}")
    return winning


def num_matches():
    balance = 0
    expenses = 0
    earnings = 0

    for i in range(1000):
        ticket = []
        for j in range(6):
            random_nums = random.randint(1, 99)
            ticket.append(random_nums)
        print(f"Ticket: {ticket}")
        balance -= 2
        expenses -= 2
        matches = []
        for i in range(len(ticket)):
            if ticket[i] == winning[i]:
                matches.append(ticket[i])
                print(f"Matches: {matches}")
                if len(matches) == 1:
                    balance += 4
                    earnings += 4
                elif len(matches) == 2:
                    balance += 7
                    earnings += 7
                elif len(matches) == 3:
                    balance += 100
                    earnings += 100
                elif len(matches) == 4:
                    balance += 50000
                    earnings += 50000
                elif len(matches) == 5:
                    balance += 1000000
                    earnings += 1000000
                elif len(matches) == 6:
                    balance += 25000000
                    earnings += 25000000

    ROI = (earnings - expenses)/expenses
    ROI *= 100
    print(f"Your current balance: ${balance}")
    print(f"Your earnings: ${earnings}")
    print(f"Your expenses: ${expenses}")
    print(f"Your ROI: {ROI}%")


pick6()
num_matches()
