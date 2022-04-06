
import random


pc_rps = ['rock','scissors','paper',]
   
pc_turn = ''
usr_ans = input('Please type rock, paper, scissors or done to exit: ')
pc_turn = random.choice(pc_rps)
if usr_ans == pc_turn:
    print('The match was a tie')
elif usr_ans =='rock' and pc_turn == 'paper':
    print('Your Kung Fu is weak')
elif usr_ans =='rock' and pc_turn == 'scissors':
    print('Your Kung Fu is strong')
elif usr_ans =='paper' and pc_turn == 'scissors':
    print('Your Kung Fu is weak')
elif usr_ans =='paper' and pc_turn == 'rock':
    print('Your Kung Fu is strong')
elif usr_ans =='scissors' and pc_turn == 'rock':
    print('Your Kung Fu is weak')
elif usr_ans =='scissors' and pc_turn == 'paper':
    print('Your Kung Fu is strong')

else:
    print('Goodbye')
