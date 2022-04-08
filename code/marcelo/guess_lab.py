import random

computer= random.randint(1,10)
trys= 0
while True:
    computer= random.randint(1,10)
    user= input('try to guess the right number: ')
    user=int(user)
    print(trys)
    if user == computer:
        print(f"correct number {user} matches {computer}, it took you {trys} attempts")
        break
    if user!=computer:
        trys += 1
        print(f'your number {user} is wrong. try again {computer}')
        print (f'you are curretly at {trys} attempts')
    # elif trys == 10:
    #     print( "you are out of your 10 attempts. byeeeee")
    #     break
