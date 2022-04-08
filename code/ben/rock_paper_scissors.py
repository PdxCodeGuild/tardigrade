import random
action = ["rock", "paper", "scissors"]
while True:
    user = input("Please choose rock, paper or scissors: ").lower()
    computer = random.choice(action).lower()
    print(f"You selected {user}, computer selected {computer}.")

    if user == computer:
        print(f"Both players selected {user}. Tie Game.")
    elif user == "rock":
        if computer == "scissors":
            print("Victory.")
        else:
            print("Defeat.")
    elif user == "paper":
        if computer == "rock":
            print("Victory.")
        else:
            print("Defeat.")
    elif user == "scissors":
        if computer == "paper":
            print("Victory.")
        else:
            print("Defeat.")

    play_again = input("Play again? (y/n) ").lower()
    if play_again == "y":
        continue
    elif play_again == "n":
        break
    else:
        print("Invalid Response. Please Run Again")
        break