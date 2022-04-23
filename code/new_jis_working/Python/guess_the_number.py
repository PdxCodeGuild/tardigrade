'''
#Version 1 

import random

y = -1
attempt = 1
while attempt <= 10:
    x = random.randint(1,10)
    print(x)
    y = int(input("Guess a number betoween 1 and 10: "))

    if x ==  y:
        print("Your guess was correct, you won!")
        break
    if attempt == 10:
        print("Game Over, you couldn't guess the  number in 10 attempts")
        break
    else:
        print("Try again")
        attempt+=1
'''



'''
#Version 2 

import random

y = -1
attempt = 1
while True:
    x = random.randint(1,10)
    print(x)
    y = int(input("Guess a number betoween 1 and 10: "))


    if x ==  y:
        print(f"Your guess was correct. You guessed {attempt} times!")
        break
    if y > 10:
        break
    else:
        print("Try again, or enter a number greater than 10 if you wish to quit")
        attempt+=1
'''

'''
#Version 3

import random

y = -1
attempt = 1
x = random.randint(1,10)

while True:
    print(x)
    y = int(input("Guess a number betoween 1 and 10: "))


    if x ==  y:
        print(f"Your guess was correct. You guessed {attempt} times!")
        break
    if y > 10:
        break
    if y > x:
        print("Too high! Try again, or enter a number greater than 10 if you wish to quit")
        attempt+=1
    else:
        print("Too low! Try again, or enter a number greater than 10 if you wish to quit")
        attempt+=1
'''