import pytest


# Write a function that returns True if the number is a double digit

def double_digit(num):
    converted = str(num)
    print(converted)
    if len(converted) > 1:
        return True

def test_double_digit():
    assert double_digit(517) == False
   
   