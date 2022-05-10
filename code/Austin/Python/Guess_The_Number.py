import random
num = int(input('Enter a number between 1 and 10:'))
guess_count = 0

while True:
    guess_count += 1
    guess = random.randint(1,10)
    if guess == num:
        print(f'Correct! You correctly guessed {guess} after {guess_count} times!')
        break
    else:
        print(f'You guess the number {guess}. Try again!')