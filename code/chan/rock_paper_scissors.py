#Chan Saechao

# Let's play rock-paper-scissors with the computer. You may want to try using these emojis 🗿📃✂️✊✋✌

#     The computer will ask the user for their choice (rock, paper, scissors)
#     The computer will randomly choose rock, paper or scissors
#     Determine who won and tell the user

import random

choice  = ['rock', 'paper', 'scissor']

repeat = True

while repeat == True:
    my_choice = input("Rock, Paper or Scissor? ")
    my_choice = my_choice.lower()
    random_number = random.randint(0,2)
    computer_choice = choice[random_number]
    

    #user is rock
    if my_choice == "rock"  and computer_choice == "rock":
        print("Rock vs Rock: Tie!")
    elif my_choice == "rock"  and computer_choice == "paper":
        print("Rock vs Paper: You Lost!")
    elif my_choice == "rock"  and computer_choice == "scissor":
        print("Rock vs Scissor: You Won!")
    #user is paper
    elif my_choice == "paper"  and computer_choice == "rock":
        print("Paper vs Rock: You Won!")
    elif my_choice == "paper"  and computer_choice == "paper":
        print("Paper vs Paper: Tie!")
    elif my_choice == "paper"  and computer_choice == "scissor":
        print("Paper vs Scissor: You Lost!")
    #user is scissor
    elif my_choice == "scissor"  and computer_choice == "rock":
        print("Scissor vs Rock: You Lost!")
    elif my_choice == "scissor"  and computer_choice == "paper":
        print("Scissor vs Paper: You Won!")
    elif my_choice == "scissor"  and computer_choice == "scissor":
        print("Scissor vs Scissor: Tie!!")
    print("\n")

    #Ask to repeat or not and return true/false if repeat or not
    question_repeat = input("Do you want to play again, yes/y or no/n: ")
    question_repeat = question_repeat.lower()
    if question_repeat == "no" or "n":
        repeat = False
    else:
        repeat = True
