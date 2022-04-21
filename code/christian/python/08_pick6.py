## Eberhardt - COMPLETE - AWAITING REVIEW

## https://github.com/PdxCodeGuild/hydra/blob/master/1%20Python/labs/08%20Pick6.md

## Have the computer play pick6 many times and determine net balance.
## Initially the program will pick 6 random numbers as the 'winner'. 
## Then try playing pick6 100,000 times, with the ticket cost and payoff below.
## A ticket contains 6 numbers, 1 to 99, and the number of matches between the 
## ticket and the winning numbers determines the payoff. Order matters, if the winning 
## numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
## If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], 
## you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

## a ticket costs $2
## if 1 number matches, you win $4
## if 2 numbers match, you win $7
## if 3 numbers match, you win $100
## if 4 numbers match, you win $50,000
## if 5 numbers match, you win $1,000,000
## if 6 numbers match, you win $25,000,000
## One function you might write is pick6() which will generate a list of 6 random numbers, 
## which can then be used for both the winning numbers and tickets. Another function could 
## be num_matches(winning, ticket) which returns the number of matches between the winning 
## numbers and the ticket.

## Steps
## Generate a list of 6 random numbers representing the winning tickets - GTG
## Start your balance at 0 - GTG
## Loop 100,000 times, for each loop: 
## Generate a list of 6 random numbers representing the ticket - GTG
## Subtract 2 from your balance (you bought a ticket) - GTG
## Find how many numbers match
## Add to your balance the winnings from your matches
## After the loop, print the final balance

import random

## Function randomly picks numbers
def pick6():
    counter = 0
    list_name = []
    while counter < 6:
        random_number = random.randrange(1,100)
        list_name.append(random_number)
        counter += 1
        if counter == 6:
            return list_name

## Generating winning numbers
winning_numbers = pick6()
# print("W Nmbrs:", winning_numbers) ##TEST STATEMENT

match_list = []

## Function compares numbers
def run_matches(winning_numbers, ticket):
    matches = 0
    idx = 0
    for num in winning_numbers:
        if num == ticket[idx]:
            matches += 1
            idx += 1
        else:
            idx +=1
            continue
    match_list.append(int(matches))

## Looping through assessment of matches 
attempts = 0
net_earnings = 0

while attempts < 100000:

    ## Generating NEW ticket
    ticket = pick6()
    # print('ticket before run matches is ran  ', ticket)  ##TEST STATEMENT

    run_matches(winning_numbers, ticket)
    attempts += 1
    net_earnings += -2
    # print("matches after  run matches is ran, entire list", match_list)  ##TEST STATEMENT
    # print("the latest match appended to list", match_list[-1])  ##TEST STATEMENT

    if match_list[-1] == 0:
        net_earnings += 0
    elif match_list[-1] == 1:
        net_earnings += 4   
    elif match_list[-1] == 2:
        net_earnings += 7  
    elif match_list[-1] == 3:
        net_earnings += 100  
    elif match_list[-1] == 4:
        net_earnings += 50000  
    elif match_list[-1] == 5:
        net_earnings += 1000000  
    elif match_list[-1] == 6:
        net_earnings += 25000000  

    # print("Net Earnings: ", net_earnings)  ##TEST STATEMENT

    if attempts >= 100000:
        print("\nTempted to buy a lottery ticket? Look at the results below!\n")
        print(f"{attempts} attempts made.")
        print(f"You're virtual net 'earnings' are: ${net_earnings}.\n") 
        break

## Notes: Yes, keeping a list of matches is a lot of data. It's possible to make this list hold only one value...
## The one value will allow the dollar amount to be determined before it is deleted and replaced with the next
## amount of matches. However, keeping a log of 'matches' allows one to go through the data and check that all 
## payments are correct. 