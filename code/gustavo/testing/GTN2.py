import random
attempts = 0
num = random.randint(1,10)
while attempts < 10:
    guess = int(input('welcome to "Guess The Number". Guess a number between 1 and 10: '))
    if guess == num:
        print('Are you psychic? You guessed it!')
        break
    elif guess > num:
        print('Too high, try again')
    elif num > guess:
        print('Too Low, try again')
    attempts = attempts + 1
    # else:
    # print('Good Try, but you need to try again')
if attempts == 10:
    print('Good try, but you didnt guess the number')