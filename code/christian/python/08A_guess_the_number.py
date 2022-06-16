# Eberhardt

## VERSION 1 - COMPLETE

## The user will then try to guess the number, and the program will tell them 
## whether they're right or wrong.

## Using a while loop, allow the user to guess 10 times. 
## If they fail to guess the number after 10 tries, the user is told they've lost. 
## If the user guesses the number, the user is told they've won and the game exits. 
## You can get a random number using random.randint:

import random
magic_number = random.randint(1,10)
guesses = 0

print("\nWELCOME TO NUMBER GUESSING GAME! V.1")

while True:
    
    if guesses < 10:
        users_guess = int(input("\nGuess the magic number: "))
        guesses += 1

        if users_guess == magic_number:
            print(f"\nYou won! You guessed {guesses} time(s).")
            break

        elif users_guess != magic_number:
            print("\nWrong...")
            continue

    elif guesses >= 10:
        print("Sorry, but you lost (-_-)")
        break

## VERSION II - COMPLETE

## Allow the user to make an unlimited number of guesses using a while True and break. 
##  Keep track of how many guesses the user has made, and tell them at the end.

import random
magic_number = random.randint(1,10)
guesses = 0

print("\nWELCOME TO NUMBER GUESSING GAME! V.2")

while True:

    users_guess = int(input("\nGuess the magic number: "))
    guesses += 1

    if users_guess == magic_number:
        print(f"Correct! You guessed {guesses} time(s).")
        break
  
    elif users_guess != magic_number:
        print("\nWrong...")
        continue
       
## VERSION III - COMPLETE
#  Tell the user whether their guess is above ('too high!') 
#  or below ('too low!') the target value.

import random
magic_number = random.randint(1,10)
guesses = 0

print("\nWELCOME TO NUMBER GUESSING GAME! V.3")

while True:

    users_guess = int(input("\nGuess the magic number: "))
    guesses += 1

    if users_guess == magic_number:
        print(f"Correct! You guessed {guesses} time(s).")
        break
  
    elif users_guess < magic_number:
        print("Guess is too low.")
        continue

    elif users_guess > magic_number:
        print("Guess is too high.")
        continue