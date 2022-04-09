# Chan Saechao
# Guess The Number

"""
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, 
and the program will tell them whether they're right or wrong.

Version 1
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. 
If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)

Below is an example run of the game:

guess the number: 5
try again!
guess the number: 2
try again!
guess the number: 3
correct! you guessed 3 times

Version 2

Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
Version 3

Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
Version 4 (optional)

Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).
Version 5 (optional)
"""

import random
computer_number = random.randint(1,10)
guess_number_max = 10
user_attempt = 0
repeat =  True
last_guess = 0

while repeat == True:
    guess_number = int(input("What number do you guess (1-10)? "))
    user_attempt +=  1
    print(f"user attempt: {user_attempt}")
    if guess_number == computer_number:
        print(f"""You Won! You guessed the correct number: {guess_number}. \nYou attempted: {user_attempt} times.""")
        break
    if guess_number + 1 == computer_number or guess_number - 1 == computer_number:
        print("You are hot!")
    if guess_number < computer_number:
        print("You are too low!")
    elif guess_number > computer_number:
        print("You are too high!")

    # Gets absolute difference of last guess/computer guess and current guess/comptuer guess
    last_guess_difference = abs(last_guess - computer_number)
    current_guess_difference = abs(guess_number - computer_number)

    # If current guess # is  less than last guess than it means the gap of number guess is getting closer to the computer number
    if last_guess != 0:
        if current_guess_difference  < last_guess_difference:
            print("Current guess is closer than previous guess.")

    last_guess = guess_number


