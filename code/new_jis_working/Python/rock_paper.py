import random

exit_game = ''
while exit_game != 'n':
    list = ['rock', 'paper', 'scissors']
    counter = 1 

    print(f'Welcome to {list}! \nYour options are:')

    for option in list:
        output = f"{counter} . {option}"

        print(output)
        counter +=1

    
    player_1 = input("Enter your selection: ")
    player_2 = random.choice(list)
    print(f'The computer selected: {player_2}')
    

    if player_1 == 'rock':
        if player_2 == 'paper':
            outcome = "you lose"
        elif player_2 == 'scissors':
            outcome = "you win"
        elif player_2 == 'rock':
            outcome = "tie"

    elif player_1 == 'paper':
        if player_2 == 'scissors':
            outcome = 'you lose'
        elif player_2 == 'rock':
            outcome = 'you win'
        elif player_2 == 'paper':
            outcome = 'tie'
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            outcome = 'you lose'
        elif player_2 == 'paper':
            outcome = 'you win'
        elif player_2 == 'scissors':
            outcome = 'tie'

    print(outcome)
    exit_game = input("Would you like to play again y/n: " )