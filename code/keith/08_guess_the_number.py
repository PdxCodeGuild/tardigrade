import random

"""
first I need to create and empty list 
then i need to make the "computer" guess a random number between 1-10 using random.randint()
then I need to have the user input a mnumber 
then i need to compare those two numbers using == 
return "right" of the user got it right and vise versa
asign an integer of 0 to a counter to keep track of guesses        +=1   end of while loop
use a print satement to tell the user if they guessed wrong? tell em when they guess right?


"""

# guess_limit = 10   ### got this idea from the googling not gonna lie
guess_count = 0
computer_guess = random.randint(1,10)

while True:
    user_geuss = int(input("Guess a number betwixt 1 and 10:  "))
    guess_count += 1
   
    if user_geuss < computer_guess:
        print("Wrong, try again, your guess was too low")
    elif user_geuss > computer_guess:
        print("wrong, try again, your guess was too high")
    elif user_geuss == computer_guess:
        print("You have guessed right, your number of guesses was: " + str(guess_count))
        break
    
        
    

# else:
#      print("You failed to guess in ten attempts, try again if you dare.....")
   