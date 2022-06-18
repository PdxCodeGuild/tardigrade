import random
import string

"""
First I need to make a randomly chosen list of 6 numbers to be the 'winning' numbers
then I need to have some sort of balance counter to keep track of spending
subtract 2 everytime I 'buy a ticket'
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
list functions for comapring two list of integers maybe .union?




"""

def pick6():    ### this function returns me a list of 6 random numbers 
    winning_number = []
    
    for number in range(6):
        random_number = random.randint(1,100)
        winning_number.append(random_number)
    return winning_number
    
def player6():     #### this function also returns me a list of 6 random numbers to be used later in for loop
    player_nums = []

    for number in range(6):
        random_number = random.randint(1,100)
        player_nums.append(random_number)
    return player_nums

def match_check(first_list, second_list):   ### this function is checking for matches in the same index postion of the two randomly made number list
    match_list = []

    for num in range(len(first_list)):
        if num in range(len(second_list)):
            if first_list[num] ==second_list[num]:
                match_list.append(num)
    return [first_list[num] for num in match_list]


print('Welcome to the lottery!!!')  #### this will be the first thing you see when you run the program



money_balance = 0   ### this gives me an empty bank to add money too and return later
plays = 100000  #### this is my tactic for setting the for loop to go 100,000 times.
for x in range(plays):   ### this is going to make sure I loop through the whole process 100,000 times
    counter = 0   #### this will be the empty counter I use to add to if my match_check function returns a value
    money = 0   ### this is the variable i'll use to store the money made then in the end subtract the 2 dollar cost
    players_ticket = player6()  ### this is assiging a variable to the use of my function 
    print(f'These are your lotto numbers: {players_ticket}')
    winning_ticket = pick6()
    print(f'The winning lotto number are: {winning_ticket}')
    matched_nums = match_check(players_ticket, winning_ticket)
    print(f'Here are the highly unlikely matches: {matched_nums}')
    for hit in matched_nums:
        counter += 1
    print(f'Here is how many highly unlikely matches you had: {counter}')
    if counter == 1:
        money += 4
    elif counter == 2:
        money += 7
    elif counter == 3:
        money += 100
    elif counter == 4:
        money += 50000
    elif counter == 5:
        money += 1000000
    elif counter == 6:
        money += 25000000
    else:
        money += 0 
    end_balance = money - 2 
    money_balance = money_balance + end_balance

cost = plays * 2
    
print(money_balance)

return_on_invesment = (money_balance - cost) / money_balance

print(f'Your ROI is: {return_on_invesment}')



   
    




   
