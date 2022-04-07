
import random

rock_paper_scissors=['rock', 'paper', 'scissors']
computer= random.choice(rock_paper_scissors)
print ('you are playing a game. please choose 1 item from the selection. "rock", "paper", and "scissors"')
user = input('choose your item: ')
if user== 'rock':
    print(f'you choose {user}')
elif user== 'scissor':
    print(f'you choose {user}')
elif user== 'paper':
    print(f'you choose {user}')
if user == computer :
    print(f"your choice {user} and the computer choice {computer} matched. its a tie!")
elif user in (rock_paper_scissors[1])!= computer in (rock_paper_scissors[0]):
    print(f"your choice {user} and the computer choice {computer} WINNER")
elif user in (rock_paper_scissors[2])!= computer in (rock_paper_scissors[0]):
    print(f"your choice {user} and the computer choice {computer} LOSER!")
elif user in (rock_paper_scissors[0])!= computer in (rock_paper_scissors[1]):
    print(f"your choice {user} and the computer choice {computer} LOSER!")
elif user in (rock_paper_scissors[2])!= computer in (rock_paper_scissors[1]):
    print(f"your choice {user} and the computer choice {computer} WINNER")
elif user in (rock_paper_scissors[0])!= computer in (rock_paper_scissors[2]):
    print(f"your choice {user} and the computer choice {computer} WINNER")
elif user in (rock_paper_scissors[1])!= computer in (rock_paper_scissors[2]):
    print(f"your choice {user} and the computer choice {computer} LOSER!")

















