
import random 

players_choices = ['rock', 'paper', 'scissors'] 

for item in players_choices: 
    

    print(item)

user_input = input('enter your selection: ')

computer = random.choice(['rock', 'paper', 'scissors']) 
print('Computer chose: ' + computer)


if user_input == computer:
    print('You Tied')

if (user_input == 'rock' and computer == 'scissors') or (user_input == 'paper' and computer == 'rock') or (user_input == 'scissors' and computer == 'paper'):
    print('You WON!!!!')

if (user_input == 'rock' and computer == 'paper') or (user_input == 'paper' and computer == 'scissor') or (user_input == 'scissors' and computer == 'rock'):
    print("You LOST!!!!:(")

