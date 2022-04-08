import random
guess_me = random.randint(0, 20)
counter = 0

while counter < 10:
    guess = int(input("What number am I thinking of? Enter a number: "))
    if guess == guess_me:
        print("You guessed it! You should probably go out and play the lottery.")
        break
    else:
        print("Wrong. Try again: ")
        print(guess_me)
        counter += 1
        if counter == 10:
            print("Game over, my friend...")
    

