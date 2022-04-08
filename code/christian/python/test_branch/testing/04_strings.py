# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text - COMPLETE
# Capitalize text and insert dashes between each letter

def loud_text(text):
    word = ("-").join(list(text)).upper()
    return(word)

def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'

# Double Letters - COMPLETE
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    double_letters_list = []
    for letter in word:
        double_letters_list.append(letter)
        double_letters_list.append(letter)
    return ("".join(double_letters_list))

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter - COMPLETE
# Count the number of letter occurances in a string

def count_letter(letter, word):
    occurrence_of_letter = []
    for item in word:
        if item == letter:
            occurrence_of_letter.append(letter)
    return len(occurrence_of_letter)

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2

# Latest Letter - COMPLETE
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    list(word).sort()
    return word[-1]

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'

# Count Hi - COMPLETE
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    return(text.count('hi')) 

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2

# Snake Case - COMPLETE
# Write a function that converts text to snake case 
# (all lowercase, underscores for spaces, no special characters).

## Reference: string.ascii_lowercase
## Reference: string.punctuation

import string   

def snake_case(text):

    legit_characters = [] 
    for char in text:
        if char in string.punctuation:
            continue
        else:
            legit_characters.append(char)

    new_text = "".join(legit_characters)
    new_text = new_text.replace(" ", "_").lower()
    return new_text

def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case 
# (no spaces, no special characters, leading capitals except the first).

import string

def camel_case(text):

    legit_characters = []
    text = text.title() 
    for char in text:
        if char in string.punctuation:
            continue
        elif char == " ":
            continue
        else:
            legit_characters.append(char)

    legit_characters[0] = str(legit_characters[0].lower())
    legit_characters = "".join(legit_characters)
    
    return legit_characters

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case - COMPELTE
# Write a function that converts text to alternating case.

def alternating_case(text):
    new_casing = []
    index = 0
    loop_breaker = 0

    while loop_breaker < len(text):
        for char in text:
            index += 1
            loop_breaker =+ 1
            if index % 2 == 1:
                char = char.upper()
                print("char upper", char)
                new_casing.append(char)
                continue
            elif index % 2 == 0:
                char = char.lower()
                new_casing.append(char)
                print("char lower", char)
                continue
        return "".join(new_casing)

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'