# Chan Saechao
# Pick 6

import random

"""
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, 
if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket 
numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. 
Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps

    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
"""

# Generate 6 random numbers as lottery numbers
def pick6():
    lottery_number = []
    for num in range(6):
        rand_num = random.randint(1,99)
        lottery_number.append(rand_num)
    return lottery_number

winning_numbers = pick6()
print(f'lottery: {winning_numbers}')

# my_ticket_numbers = pick6()
# print(my_ticket_numbers)

# TAke in 2 list of numbers that is the winning list and ticket number list and match them
# def num_matches(winning, ticket):
#     match_nums = 0
#     # Loops through both 
#     for winning_num in winning:
#         for ticket_num in ticket:
#             if winning_num == ticket_num:
#                 match_nums += 1
#     if match_nums == 1:
#         print(f"{match_nums} matching number.")
#     elif match_nums > 1:
#         print(f"{match_nums} matching numbers.")
#     else:
#         print("No matching numbers.")
#     return match_nums

# num_matches(winning_numbers, my_ticket_numbers)


# Version 2

# Balance
balance = 0
earnings = 0
expenses = 200000

# TAke in 2 list of numbers that is the winning list and ticket number list and match them
def num_matches(winning, ticket, balance, earnings):
    match_nums = 0
    count = 0
    # Loops through both 
    for winning_num in winning:
        # print(winning_num)
        if winning[count] == ticket[count]:
            match_nums += 1
            # print("match")
        # print(winning[count], ticket[count])
        count += 1

    # Calculate winnings of each ticket matches to balance
    if match_nums == 1:
        balance += 4
        earnings += 4
    elif match_nums == 2:
        balance += 7
        earnings += 7
    elif match_nums == 3:
        balance += 100
        earnings += 100
    elif match_nums == 4:
        balance += 50000
        earnings += 50000
    elif match_nums == 5:
        balance += 1000000
        earnings += 1000000
    elif match_nums == 6:
        balance += 25000000
        earnings += 25000000
    else:
        balance += 0

    # Subtract 2 for ticket
    balance -= 2

    results = [balance, earnings]

    # print(f"balance after {balance}")
    return results

# num_matches(winning_numbers, my_ticket_numbers, balance)

# Loop through 100,000 lottery tickets
# print(f'balance before {balance}')
ticket_count = 0
attempts = 100000
expenses = attempts * 2
while ticket_count < attempts:
    # print(f"Ticket #: {ticket_count + 1}")
    my_ticket_numbers = pick6()
    # print(f'lottery: {winning_numbers}')
    # print(my_ticket_numbers)
    balance_earning_list = num_matches(winning_numbers, my_ticket_numbers, balance, earnings)
    balance = balance_earning_list[0]
    earnings = balance_earning_list[1]
    # print(balance)
    # print(ticket_count)
    ticket_count += 1

# print(f'Balance After: {balance} earnings: {earnings}')
roi = (earnings - expenses)/earnings
print(f'Earnings: {earnings} Expenses: {expenses} Return of investments: {roi}')

