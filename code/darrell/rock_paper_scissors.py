import random

#ask the user for their choice of rock, paper, or scissors
user_choice = input("Please enter 'Rock', 'Paper', or 'Scissors': ")

#allow the computer to randomly select between rock, paper, or scissors
rps_list = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(rps_list)
print(user_choice)
print(computer_choice)

if user_choice == "Rock" and computer_choice == "Rock":
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Paper":
    print("You lost!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You won!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You won!")
elif user_choice == "Paper" and computer_choice == "Paper":
    print("It's a tie!")
elif user_choice == "Paper" and computer_choice == "Scissors":
    print("You lost!")
elif user_choice == "Scissors" and computer_choice == "Rock":
    print("You lost!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You won!")
elif user_choice == "Scissors" and computer_choice == "Scissors":
    print("It's a tie!")

