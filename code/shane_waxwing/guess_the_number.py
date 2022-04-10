import random
guess_me = random.randint(0, 20)
counter = 0

#--------------------------------------------------------------------------------#

while True:
    guess = int(input("What number am I thinking of? Enter a number: "))
    if guess == guess_me:
        print(f"You guessed it!. It took you {counter} guess(es)")
        break
    else:
        print("Wrong. Try again: ")
        counter += 1
    

