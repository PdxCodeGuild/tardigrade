def main():
    import random
    rps = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    win = {
        'scissors': ['rock', 'spock'],
        'rock': ['paper', 'spock'],
        'paper': ['scissors', 'lizard'],
        'lizard': ['rock', 'scissors'],
        'spock': ['paper','lizard']
        }
    computer = random.choice(rps)

    print('Welcome to Rock, Paper, Scissors!')
    for options in rps:
        print(options)
    player = input('Enter your selection:')

    if player == computer:
        print(f'You chose: {player}\nComputer Chose: {computer}\nOutcome: Tie')
    elif player in win[computer]:
        print(f'You chose: {player}\nComputer Chose: {computer}\nOutcome: You Win')
    else:
        print(f'You chose: {player},\nComputer Chose: {computer},\nOutcome: You Lose')


    replay = True
    while replay:
        play_again = input('Would you like to play again? Enter yes or no:')
        if play_again == 'yes':
            main()
        else:
            print('Game_Over')
            break

main()