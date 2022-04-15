# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

import string 

def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word

def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    return ''.join(x * 2 for x in word)

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string


def count_letter(letter, word):
    return word.count(letter)

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    x = list(word)
    reversed(sorted(x))
    return x[0]

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    x = 'hi' 
    return text.count(x)


def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    x = list(text)
    for i in x:
        if i in string.punctuation:
            x.remove(i)
    return ''.join(x).replace(" ", "_").lower()


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    y = str(text).title()
    x = list(y)
    for i in x:
        if i in string.punctuation:
            x.remove(i)
        if i == ' ':
            x.remove(i)
    x[0] = str(x[0].lower())
    return ''.join(x)


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text): 
    x = text[0::2].upper()
    y = text[1::2].lower()
    return ''.join(map(''.join, zip(x, y)))


def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'