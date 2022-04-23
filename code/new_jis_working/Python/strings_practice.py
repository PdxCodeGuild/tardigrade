

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

from re import ASCII


def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'

#Passed_______________________________________________________________________________________________________________###################

# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    new_word = ""
    for x in word:
        new_word = new_word + (x+x)
    
    return new_word

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

#Passed_______________________________________________________________________________________________________________###################

# Count Letter
# Count the number of letter occurances in a string



def count_letter(letter, word):
    new_word = [ ]
    for x in word:
        if x == letter:
            new_word.append(letter)
    return len(new_word)


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2

#Passed_______________________________________________________________________________________________________________###################


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    word = sorted(word)
    return word[-1]


def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'

#Passed_______________________________________________________________________________________________________________###################

# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    no_space = text.replace(" ", "")
    hi_list = no_space.replace("hi","1")
    
    count_list = [ ]
    
    for x in hi_list:
        if x == '1':
            count_list.append(x)
    return len(count_list)


def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2

#Passed_______________________________________________________________________________________________________________###################

# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters)

import string


def snake_case(text):
    lower_case = text.casefold().replace(" ", "_")
    
    special_character = ",./?!@#$%^&*()+=-[}]{:;|"

    for x in lower_case:
        snake_case = lower_case
        
        for y in special_character:
            if x == y:
                snake_case = snake_case.replace(y, "")
    return snake_case   


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

#Passed_______________________________________________________________________________________________________________###################

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).


def camel_case(text):
    
    text_c = text.title()
    lower_list = list(text_c)
    lower_list[0] = lower_list[0].swapcase()
            
    camel_string = "".join(lower_list)
    final_string = camel_string.replace(" ", "")
    special_character = "!,./?@#$%^&*()+=-[}]{:;|"
    
    for x in final_string:
        for y in special_character:
            if x == y:
                final_string = final_string.replace(y, "")
    return final_string




def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

#Passed_______________________________________________________________________________________________________________###################

# Alternating Case
# Write a function that converts text to alternating case.


def alternating_case(text):
    
    swap_list = list(text)
    join_list = [ ]
    pointer_a = 0
    pointer_b = 1

    
    while len(join_list) < len(swap_list):
        join_list.append(swap_list[pointer_a].upper())
        join_list.append(swap_list[pointer_b].lower())
        pointer_a+=2
        pointer_b+=2
    return "".join(join_list)  

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'