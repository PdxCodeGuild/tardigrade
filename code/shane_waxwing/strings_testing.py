

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    word = ("-").join(list(text.upper()))
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    new_list= []

    for letter in word:
        new_list.append(letter)
        new_list.append(letter)
    return "".join(new_list)

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'


# Count Letter
# Count the number of letter occurances in a string


def count_letter(letter, word):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    biggest_letter = ""
    for letter in word:
        if letter > biggest_letter:
            biggest_letter = letter
    return biggest_letter




def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):

    counter = 0
    index = 0
    while text.find("hi", index) != -1:
       index = text.find("hi", index) +1
       counter += 1
    return counter


    

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):

    snake = text.lower()
    
    
    for letter in text:
        if not letter.isalnum() and  letter != " ":
            snake = snake.replace(letter, "")
    
    snek = snake.replace(" ", "_")
    
    
    return snek






def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'



# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).


def camel_case(text):
    
    
    camel = text.lower()

    
    for char in text:
        if not char.isalpha() and char != " ":
            camel = camel.replace(char, "")
            
    
    almost_camel_list = camel.split()
    almost_camel_list_2 = []
    for item in almost_camel_list:
        almost_camel_list_2.append(item.title())
    almost_camel_list_2[0] = almost_camel_list_2[0].lower()

    almost_camel = "".join(almost_camel_list_2)
    
    return almost_camel

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'








# Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    text = text.lower()
    text_2 = []
    for i in range(len(text)):
        if i%2 == 0:
            text_2.append(text[i].swapcase())
        else: text_2.append(text[i])
    text_2 = "".join(text_2)
    return text_2
    
def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'

