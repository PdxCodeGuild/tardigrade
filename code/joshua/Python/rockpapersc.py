import random

def game_init():
    print('Hello nerd Thanks for playing my game')

def game_choices():
    game_option = False
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    # print('These are the following choices:')
    


    print('Please select a postions from the following choices...')
    for x,y in choices.items():
        print(f'Choose {x} for {y}')
    
    while game_option == False:
        user_choice = input('Please type the digit form of your selected choice\n')
        if user_choice == ('1') or user_choice == ('2') or user_choice == ('3'):
            user_choice = int(user_choice)
            break
            
            
        else:
            print('Sorry choose a correct option')
        
    global_choice = choices[user_choice]
    return global_choice
        


def comp_positon():
    comp_number = random.randint(1,3)
    if comp_number == 1:
        comp_choice = 'Rock'
    elif comp_number == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = "Scissors"
    
   
    return comp_choice







def game_decision(user_option, comp_option):
    if user_option == 'Rock' and comp_option == 'Rock':
        print(f'''Damn the game resulted in a tie\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Rock' and comp_option == 'Paper':
        print(f'''You suck :( you lost the game\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Rock' and comp_option == 'Scissors':
        print(f'''Damn look at you, Youre smarter than a computer\n
        You got {user_option} and the computer got {comp_option}''')
    
    elif user_option == 'Paper' and comp_option == 'Paper':
        print(f'''Damn the game resulted in a tie\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Paper' and comp_option == 'Scissors':
        print(f'''You suck :( you lost the game\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Paper' and comp_option == 'Rock':
        print(f'''Damn look at you, Youre smarter than a computer\n
        You got {user_option} and the computer got {comp_option}''')
    
    
    
    elif user_option == 'Scissors' and comp_option == 'Scissors':
        print(f'''Damn the game resulted in a tie\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Scissors' and comp_option == 'Rock':
        print(f'''You suck :( you lost the game\n
        You got {user_option} and the computer got {comp_option}''')
    elif user_option == 'Scissors' and comp_option == 'Paper':
        print(f'''Damn look at you, Youre smarter than a computer\n
        You got {user_option} and the computer got {comp_option}''')
    









game_init()
user_option = game_choices()
comp_option = comp_positon()
game_decision( user_option, comp_option )