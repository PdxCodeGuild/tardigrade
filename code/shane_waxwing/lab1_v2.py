import random

adj = input("Enter an adjective: ")

noun_string = input('Enter ten nouns separated by ",": ')
noun_list = noun_string.split(', ')

pverb_string = input('Enter four past tense verbs separated by ",": ')
pverb_list = pverb_string.split(', ')

madlib = (f"""\nI {random.choice(pverb_list)} up to find the {random.choice(noun_list)} was {adj} one day
And all around the {random.choice(noun_list)}, now, things began to change
Never had I ever {random.choice(pverb_list)} the {random.choice(noun_list)}
Rise that way above the {random.choice(noun_list)} to greet the {random.choice(noun_list)}

And the {random.choice(noun_list)} shook beneath my {random.choice(noun_list)}
And the {random.choice(noun_list)} raged through the {random.choice(noun_list)}
And I lost all that I had {random.choice(pverb_list)}
Oh, but I {random.choice(pverb_list)} like the {random.choice(noun_list)}""")

print(madlib)