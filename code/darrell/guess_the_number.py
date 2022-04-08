import random
random_number = random.randint(1, 10)
print(random_number)


x = 0
while x < 10:
    user_guess = input("Guess a number between 1 and 10: ")
    user_guess = int(user_guess)
    if user_guess == random_number:
        print(f"Congrats, you guessed the number! You guessed {x+1} times.")
        break
    else:
        print("Please guess again!")
    x += 1
print(f"Sorry, you're out of guesses! You guessed more than {x} times.")
