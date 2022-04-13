
#change
# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

# from pyparsing import Word


def double_letters(word):
    doubled_word = []
    for letter in word:
        doubled_word.append(letter +''+ letter)
    return ''.join(doubled_word)



   


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# # Count Letter
# # Count the number of letter occurances in a string


# my_string = ""
#     for x in range(0,n):
#         my_string += "*"
#     return my_string
#####
#### loop through the letters of the word
#### if statement on the letter to see if its i
#### if it is i then increment a new variable by 1

def count_letter(letter, word):
    final_count = [] ##### establishing an empty list
    for letter_2 in word: #### iterate through the word
        if letter_2 == letter:  ####### if a character in the word is == the letter 
            final_count.append(1) ### add 1 to the list
    return(len(final_count)) #### return the number of elements in the list
            
            


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
         'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


 #### use len() -1 hello [len (hello)-1]

# Latest Letter
#Return the letter that appears the latest in the english alphabet.
def latest_letter(word):
    answer = sorted(word)
    return answer[-1]
   



def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    counter = 0 ##### this is the counter set up initally as 0 
    temp_string = "" #### this is the empty string to manipulate
    for character in text:  ###### this is the loop going through the string perameter
        if character == 'h': ##### checking if one of the character is h
            temp_string = character ##### if its an h were adding it to temp_string
        elif character == 'i':  ##### checking is one of the chacters is i 
            if temp_string == 'h':  ##### seeing if the i was preceeded by an h
                counter += 1  #### adds one to the counter
        else:  #### else if triggererd if not an h or an i
            temp_string = ""  #### clear out the temp
    return counter  ##### returns the value in the counter




def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).
# .lower .replace .remove?

"""
1st I need to go through the string maybe using a for loop
2nd I need to check for spaces and replace them with underscores _
3rd I need to covert the whole list into lowercase because snake_case has no uppercase
4th I need to check for special characters and remove them
5th I need to return that new string 

# """

import string


def snake_case(text):
    final_phrase = ""  ### creating an empty string for me to add to later
    
    text = text.lower()  ##### this is making the whole string lowercase
    # print(text)
    punctuation = list(string.punctuation)  #### this is making a list of all of the punctuation marks to elim
    for character in text:
        if character not in punctuation:
            final_phrase += character
        
    final_phrase = final_phrase.replace(" ", "_")       

    return final_phrase
  
        
            
        # print(text)

def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'
            
  
        







# # Camel Case
# # Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).
# """
# 1st I need to eliminate uppercase expect the first?
# 2nd I need to eliminate spaces
# 3rd I need to eliminate special characters
# 4th I need to return the return the new string
# 5th I need 

# """


import string


def camel_case(text):
    final_phrase = ""
    text = text.lower()
    punctuaion = list(string.punctuation)
    for char in text:
        if char  not in punctuaion:
            final_phrase += char
    updated = list(final_phrase)
    for character in range(len(updated)):
        if updated[character] == ' ':
            updated[character+1] = updated[character+1].upper() 
            # print(character, "check here")
    converted_list = "".join(updated)
    last_word = converted_list.replace(" ", "")

    print(last_word)

   
     
    return last_word

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case
# Write a function that converts text to alternating case.

"""
iterate through the list
maybe use %
use indeces and +1 
.upper?



"""


def alternating_case(text):
    final_phrase = ''   #### gives me a string to put characters in and output in the end
    for char in range(len(text)):    #### loops over my perameters "Hello World!"
        if char % 2 == 0: #### using modulo to find is the remainder is zero thus making it an even number
            final_phrase = final_phrase + (text[char].upper())  ### uppercases the characer if it is  
        else:
            final_phrase = final_phrase + (text[char].lower())   ### lowercases the character if it is
            
    
    return final_phrase


def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'





