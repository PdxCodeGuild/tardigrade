import random

count = 0
x = random.randint(1,10) 
while True:
    user = int(input("Please enter a number: "))
    print(f"You selected {user}")
    
    if user == x:
        print("You won! The game is now over")
        break
    elif user > x:
        count += 1
        print("Your guess is too high! Try again.")
        print(f"That was attempt number: {count}.")
    else:
        count += 1
        print("Your guess is too low! Try again.")
        print(f"That was attempt number: {count}.")
    
    try_again = input("Would you like to try to again? (y/n):").lower()
    if try_again == 'y':
            continue
    elif try_again == 'n':
        break
    else:
        continue