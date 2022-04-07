# Eberhardt - MadLib

# INSTRUCTIONS:
# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.

print('\n===WELCOME TO MADLIB!===\n')

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')
body_part = input('Name a body part: ')

print(f'''\nTHE BEST STORY EVER TOLD:\n
Long ago, in a galaxy far far away.... lived a {noun}!
But this was no ordinary {noun}, this was one that could {verb}.
And so the {adjective} {noun} made sure to {verb} {adverb} as best as it could!
...until one day its {body_part} blew up into a million pieces.

***Your credit card will now be charged $1M for use of this MadLib app.***
''')


# Version 2
# Make a functional solution that utilizes lists. 
# For example, ask the user for 3 adjectives, separated by commas, 
# then use the .split() function to store each adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which 
# adjective goes where in the story.

# import random

# adjective_list = []
# randomized_adjective_order = []

# print('''
# ===Welcome to MadLibs===
# -------Version II-------
# ''')

# adjectives = input('''Enter 3 adjectives separated by commas.
# Ex: adjective, adjective, adjective
# Enter here: ''')

# adjectives.split(', ')
# adjective_list.append(adjectives)

# while True:
#     if adjective_list is not []:
#         adjective_placer = random.choice(adjective_list)
#         randomized_adjective_order.append(adjective_placer)
#     else:
#         break
    
# print(f'''
# The car was {randomized_adjective_order[0]}
# and {randomized_adjective_order[1]} 
# and {randomized_adjective_order[2]}.''')