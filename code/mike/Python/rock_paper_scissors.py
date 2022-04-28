import random

options = ['rock', 'paper', 'scissors']

print()
print('How about a friendly game of Rock, Paper, Scissors?')

print()
print('Your options are:')

for option in options:
    print(f"- {option.title()}")

print()
user_choice = input('Enter your selection:')

print()

computer_choice = random.choice(options)

print(computer_choice)

if computer_choice == 'rock' and user_choice == 'paper':
    print()
    print('human wins'.title())
elif computer_choice == 'paper' and user_choice == 'scissors':
    print()
    print('human wins'.title())
elif computer_choice == 'scissors' and user_choice =='rock':
    print()
    print('human wins'.title())
elif computer_choice == 'rock' and user_choice =='scissors':
    print()
    print('computer wins'.title())
elif computer_choice == 'paper' and user_choice =='rock':
    print()
    print('computer wins'.title())    
elif computer_choice == 'scissors' and user_choice =='paper':
    print()
    print('computer wins'.title())
else:
    print()
    print('tie'.title())