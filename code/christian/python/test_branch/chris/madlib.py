# Eberhardt - MadLib

# VERSION 1

# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.

# print('\n===WELCOME TO MADLIB!===\n')

# noun = input('Enter a noun: ')
# verb = input('Enter a verb: ')
# adjective = input('Enter an adjective: ')
# adverb = input('Enter an adverb: ')
# body_part = input('Name a body part: ')

# print(f'''\nTHE \"BEST\" STORY EVER TOLD:\n
# Long ago, in a galaxy far far away.... lived a {noun}!
# But this was no ordinary {noun}, this was one that could {verb}.
# And so the {adjective} {noun} made sure to {verb} {adverb} as best as it could!
# ...until one day its {body_part} blew up into a million pieces.

# ***Your credit card will now be charged $1M for use of this MadLib app.***
# ''')

# ----------------------------------------------------------------------------#

# VERSION 2

# Make a functional solution that utilizes lists. 
# For example, ask the user for 3 adjectives, separated by commas, 
# then use the .split() function to store each adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which 

# import random

# print('''
# ===Welcome to MadLibs===
# -------Version II-------
# ''')

# adjectives = input('''Enter 3 adjectives separated by commas.
# Ex: adjective,adjective,adjective

# Enter here: ''')

# adjectives_list = adjectives.split(',')
# number = random.randint(1, 3)

# if number == 1:
#     place_1 = adjectives_list[0]
#     place_2 = adjectives_list[1]
#     place_3 = adjectives_list[2]
# elif number == 2:
#     place_1 = adjectives_list[2]
#     place_2 = adjectives_list[0]
#     place_3 = adjectives_list[1]
# elif number == 3:
#     place_1 = adjectives_list[1]
#     place_2 = adjectives_list[2]
#     place_3 = adjectives_list[0]

# print(f'''\nHave you ever seen a {place_1} dinosaur? Neither have I!
# Just imagine your face upon seeing such a sight!
# Yep, your face would probably be all {place_2} and what not.
# Anywho, I guess it's time to stop daydreaming and be a responsible dad...

# ...wait... where did my {place_3} kids go???
# ''')

# ----------------------------------------------------------------------------#

# VERSION 3

# Make it repeatable. Once you're done prompting the user... 
# prompt them for whether they'd like to hear the story. 
# Use a while loop to keep asking if they'd like to hear the story until the answer is 'no'.
#  You could then ask them if they'd like to make another story, and so on.

import random

print('''
===Welcome to MadLibs===
-------Version II-------''')

while True:

    def madlib():
        number = random.randint(1, 3)

        if number == 1:
            place_1 = adjectives_list[0]
            place_2 = adjectives_list[1]
            place_3 = adjectives_list[2]
        elif number == 2:
            place_1 = adjectives_list[2]
            place_2 = adjectives_list[0]
            place_3 = adjectives_list[1]
        elif number == 3:
            place_1 = adjectives_list[1]
            place_2 = adjectives_list[2]
            place_3 = adjectives_list[0]

        print(f'''\nHave you ever seen a {place_1} dinosaur? Neither have I!
Just imagine your face upon seeing such a sight!
Yep, your face would probably be all {place_2} and what not.
Anywho, I guess it's time to stop daydreaming and be a responsible dad...

...wait... where did my {place_3} kids go???
''')
        play_again = input('Would you like to hear ANOTHER story? y/n')
        if input.lower() == 'y':
            
        else:
            print("I get it... that last story was pretty bad....")




    adjectives = input('''
Enter 3 adjectives separated by commas.
Ex: adjective,adjective,adjective

Enter here: ''')

    p

    adjectives_list = adjectives.split(',')
    users_choice = input('\nWould you like to hear a story? y/n ')

    if users_choice.lower() == 'y':
        madlib()
    else:
        print('\nYeah... that\'s the \'story\' of my life...')
        break

    