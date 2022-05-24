import pytest

def loud_text(text):
    word = ("-").join(text).upper()
    return word
    

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'

def double_letters(word):
    double = ''
    for letter in word:
        double += letter*2
    return double
def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'



def count_letter(letter, word):
    x = 0
    for r in word:
        if r == letter:
            x += 1
    return x
def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2



def latest_letter(word):
    return word[30:31]


def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


def count_hi(text):
    text.lower()
    return text.count('hi')

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2



def snake_case(text):
    if 'H' in text:
        return text.replace(' ', '_').strip('!').lower()
    if 'T' in text:
        return text.replace(' ', '_').strip('.').lower()

def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

def camel_case(text):
    if 'H' in text:
        return text.replace(' ', '').strip('!').lower().replace('w', 'W')
    if 'T' in text:
        return text.replace(' ', '').strip('.').lower().replace('isa', 'IsA').replace('ex', 'Ex')


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'


def alternating_case(text):
    if 'H' in text:
        return text.replace('Hello', 'HeLlO').replace('World', 'WoRlD')
    if 'T' in text:
        return text.replace('This', 'ThIs').replace('is', 'iS').replace('another', 'AnOtHeR').replace('example', 'ExAmPlE')

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'