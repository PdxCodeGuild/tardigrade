import random

choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
comp_choice = random.choice(choices)
play_again = 'y'


while play_again == 'y':
    user_choice = input(f"Please choose one of the following: {choices}\n")

    #-------------------------User picks rock----------------------------------#

    if user_choice == "rock" and comp_choice == "rock":
        print(f"{comp_choice}: It's a tie!")
    elif user_choice == "rock" and comp_choice == "paper":
        print(f"{comp_choice}: Paper covers rock! You lose!")
    elif user_choice == "rock" and comp_choice == "scissors":
        print(f"{comp_choice}: Rock smashes scissors! You win!")
    elif user_choice == "rock" and comp_choice == "lizard":
        print(f"{comp_choice}: Rock crushes lizard! You win!")
    elif user_choice == "rock" and comp_choice == "spock":
        print(f"{comp_choice}: Spock vaporizes rock! You lose!")

    #----------------------------------User picks paper-------------------------------------#

    elif user_choice == "paper" and comp_choice == "paper":
        print(f"{comp_choice}: It's a tie!")
    elif user_choice == "paper" and comp_choice == "rock":
        print(f"{comp_choice}: Paper covers rock! You win!")
    elif user_choice == "paper" and comp_choice == "scissors":
        print(f"{comp_choice}: Scissors cuts paper! You lose!")
    elif user_choice == "paper" and comp_choice == "lizard":
        print(f"{comp_choice}: Lizard eats paper! You lose!")
    elif user_choice == "paper" and comp_choice == "spock":
        print(f"{comp_choice}: Paper disproves spock! You win!")

    #--------------------------------User picks scissors----------------------------------#

    elif user_choice == "scissors" and comp_choice == "rock":
        print(f"{comp_choice}: Rock smashes scissors. You lose!")
    elif user_choice == "scissors" and comp_choice == "paper":
        print(f"{comp_choice}: Scissors cuts paper! You lose!")
    elif user_choice == "scissors" and comp_choice == "scissors":
        print(f"{comp_choice}: It's a tie!")
    elif user_choice == "scissors" and comp_choice == "lizard":
        print(f"{comp_choice}: Scissors decapitates lizard")
    elif user_choice == "scissors" and comp_choice == "spock":
        print(f"{comp_choice}: Spock smashes scissors! You lose!")

    #-------------------------------User picks lizard---------------------------------------#

    elif user_choice == "lizard" and comp_choice == "rock":
        print(f"{comp_choice}: Rock crushes lizard. You lose!")
    elif user_choice == "lizard" and comp_choice == "paper":
        print(f"{comp_choice}: Lizard eats paper. You win!")
    elif user_choice == "lizard" and comp_choice == "scissors":
        print(f"{comp_choice}: Scissors decapitates lizard. You lose!")
    elif user_choice == "lizard" and comp_choice == "lizard":
        print(f"{comp_choice}: It's a tie!")
    elif user_choice == "lizard" and comp_choice == "spock":
        print(f"{comp_choice}: Lizard poisons Spock. You win!")

    #-------------------------------User picks Spock----------------------------------------#

    elif user_choice == "spock" and comp_choice == "rock":
        print(f"{comp_choice}: Spock vaporizes rock. You win!")
    elif user_choice == "spock" and comp_choice == "paper":
        print(f"{comp_choice}: Paper disproves Spock! You lose!")
    elif user_choice == "spock" and comp_choice == "scissors":
        print(f"{comp_choice}: Spock smashes scissors. You win!")
    elif user_choice == "spock" and comp_choice == "lizard":
        print(f"{comp_choice}: Lizard poisons Spock. You lose.")
    elif user_choice == "spock" and comp_choice == "spock":
        print(f"{comp_choice}: It's a tie!")
    #__________________________________________________________________________________________#

    play_again = input('Would you like to play again? y/n')

print("Thanks for playing ^_^")