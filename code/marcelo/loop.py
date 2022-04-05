import pytest

def double_numbers(nums):
    new_list= []
    for num in nums:
        new_list.append(num + 3)
    return new_list

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [4, 5, 6]

def stars(n):
    return (n*'*')

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'

def extract_less_than_ten(nums):
    new_list= []
    for num in nums:
        new_list.append(nums)
        new_list.pop(2)
        new_list.pop(3)
    return new_list

def test_extract_less_than_ten(nums):
    extract_less_than_ten([2, 8, 12, 18]) == [2, 8]