import random
last_guess = 0
last_guess_ls = []
attempts = 0
num = random.randint(1,10)
while attempts < 10:
    guess = int(input('welcome to "Guess The Number". Guess a number between 1 and 10: '))
    attempts += 1
    print(attempts)
    if attempts >= 2:
        print(num)
        last_guess_ls.clear()
        tv1 = abs(guess - num)
        # print(tv1,'This is the first value tv1')
        last_guess_ls.append(tv1)
        tv2 = abs(last_guess - num)
        # print(tv2,'This is the second value tv2')
        last_guess_ls.append(tv2)
        # min(last_guess_ls[0,1])
        print(last_guess_ls[0])
        print(last_guess_ls[1])
        if last_guess_ls[0] > last_guess_ls[1]:
            print('getting colderr, try again!')
        elif last_guess_ls[0] < last_guess_ls[1]:
            print('getting warmer, try again!')
    # elif  min(abs(guess - num) < (abs(last_guess - num))):
    #     print('getting colder, try again!')
    else:
        continue
    if guess == num:
        print('Are you psychic? You guessed it!')
        break
    elif guess > num:
        print('Too high, try again')
    elif num > guess:
        print('Too Low, try again')
    
    # print(attempts)
    last_guess = guess
    
if attempts == 10:
    print('Good try, but you didnt guess the number')