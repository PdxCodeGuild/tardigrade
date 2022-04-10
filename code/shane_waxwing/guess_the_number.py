import random
guess_me = random.randint(0, 100)
counter = 0

#--------------------------------------------------------------------------------#

while True:
    guess = int(input("What number am I thinking of? Enter a number: "))
    if guess == guess_me:
        counter += 1
        print(f"You guessed it!. It took you {counter} guess(es)")
        break
    elif guess < guess_me:
        counter += 1
        print(f"Number of Guesses: {counter}")
        print("Too low! Try again!")
    elif guess > guess_me:
        counter += 1
        print(f"Number of Guesses: {counter}")
        print("Too high! Try again!")
    