import pytest


# Go Hiking
# Write a function that takes a string indicating energy level and weather

def go_hiking(energy, weather):
    if energy == "tired" and weather == "rainy":
        return False
    elif energy == "tired" and weather == "sunny":
        return False
    elif energy == "spry" and weather == "rainy":
        return False
    elif energy == "spry" and weather == "sunny":
        return True

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    #convert num to absolute numbers
    abs_num = abs(num)
    print(abs_num)
    #convert abs_num to a string
    string_num = str(abs_num)
    l = len(string_num)
    print(l)
    if l == 2:
       return True
    else:
        return False


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.
    
def opposite(a, b):
    if a>0 and b<0:
        return True
    elif a<0 and b>0:
        return True
    else:
        return False
    


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False