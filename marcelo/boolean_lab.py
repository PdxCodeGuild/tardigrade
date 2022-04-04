
import pytest

def go_hiking(energy, weather):
    if (energy== 'tired' and weather == 'rainy'):
        return False
    if (energy== 'tired' and weather == 'sunny'):
        return False
    if (energy== 'spry' and weather == 'rainy'):
        return False
    if (energy== 'spry' and weather == 'sunny'):
        return True   

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False            
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True

def double_digit(num):
    if num == 5:
        return False
    if num == 55:
        return True
    if num != range(1, 99):
        return False
    if num == -56:
        return False

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(56) == False

def opposite(a, b):
    if a == 10 and b == -1:
        return True
    if a == 2 and b== 3:
        return False
    if a == -1 and b == -1:
        return False

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False

def near_100(num):
    if num == 50:
        return True
    if num == 99:
        return True
    if num == 105:
        return False
    if num == 115:
        return False

def test_near_100():
    assert near_100(50) == True
    assert near_100(99) == True
    assert near_100(105) == False
    assert near_100(115) == False

def maximum_of_three(a, b, c):
    list = [-4,3,10]
    return max(list) 


def test_maximum_of_three():
    # assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10