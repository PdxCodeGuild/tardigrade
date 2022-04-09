import pytest


def go_hiking(energy, weather):
    if (energy, weather) == ('spry', 'sunny'):
        return True
    if (energy, weather) == ('tired', 'rainy') or ('tired', 'sunny') or ('spry', 'rainy'):
        return False
   
        

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True









