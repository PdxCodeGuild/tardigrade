import random
attempts = 0
num = random.randint(1,10)
while attempts < 10:
    guess = int(input('welcome to "Guess The Number". Guess a number between 1 and 10: '))
    if guess == num:
        print('Are you psychic? You guessed it!')
        break
    else: attempts = attempts + 1 
    print('Good Try, but you need to try again')
if attempts == 10:
    print('Good try, but you didnt guess the number')