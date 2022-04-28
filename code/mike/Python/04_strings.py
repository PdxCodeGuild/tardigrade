import pytest

# # Practice 4: Strings
# # Copy and paste this file into your own "04_strings.py"
# # Fill in the code for each of the functions
# # Run the tests by typing "pytest 04_strings.py"

# # Loud Text
# # Capitalize text and insert dashes between each letter

def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# # # # Double Letters
# # # # Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    new_word = ''
    for chr in word:
        new_word += chr*2
    return new_word


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# # # # # Count Letter
# # # # # Count the number of letter occurances in a string


def count_letter(letter, word):
    counter = 0
    for i in word:
        if i == letter:
            counter += 1
    return counter

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2



# # # # # Latest Letter
# # # # # Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    word = ''.join(sorted(word))
    return word[-1]


def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# # # Count Hi
# # # Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
   hi = text.count('hi')
   return hi


def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# # # Snake Case
# # # Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).
# ## Build a list to compare letters in text against to see if they are punctuation or not
# ## Store those letters in a list or variable for the return statement
# import string



def snake_case(text):
    set_punctuation = string.punctuation
    new_text = " "
    for char in text:
        if char not in set_punctuation:
            new_text += char
    print(new_text)    
    return "_".join(new_text.lower().split())


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'


# # # Camel Case
# # # Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

import string

def camel_case(text):
    new_string = " "
    for letter in text:
        if letter == ' ':
            counter += 1
        elif counter == 1:
            new_string += letter.upper()
            counter == 0
        elif letter in string.punctuation:
            continue
        else:
            new_string += letter.lower()
        return new_string
        

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'


# # # Alternating Case
# # # Write a function that converts text to alternating case.

def alternating_case(text):
    index = 0
    result = ''
    swap = text.swapcase()

    for letter in swap:
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        index += 1
    return result


def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'