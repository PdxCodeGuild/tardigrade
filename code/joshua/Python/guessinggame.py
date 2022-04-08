import random


def u_vs_cpu():
    cpu_choice = random.randint(1,50)
    user_tries = 10
    user_choice = int(input('Hello\nPlease choose a number 1-50.... arigato...BTW you only have 10 tries hehehehhee\n'))
    while True:
        if user_tries == 1:
            print('It took you every try just to fail... better luck next time')
            break
        
        elif user_choice == cpu_choice:
            print(f'Congrats!!!! You beat the computer\nYou had {user_tries} tries left. Good Job')
            break
        
        elif user_choice < cpu_choice:
            # user_tries -= 1
            print(f'Too Low, You were {abs(cpu_choice - user_choice)} away from the computer, try again please \n{user_tries} tries left')
            
            user_choice = int(input('Please choose a number 1-10\n'))
            
        
        elif user_choice > cpu_choice:
            # user_tries -= 1
            print(f'Too High, You were {abs(cpu_choice - user_choice)} away from the computer, try again please \n{user_tries} tries left')
            
            user_choice = int(input('Please choose a number 1-10\n'))
        
        user_tries -= 1

u_vs_cpu()
