import pytest
# def double_letters():
#     dubdub = ''
#     word = input('please enter letters ')
#     for letter in word:
#         dubdub += letter*2
#     return dubdub

# #     for letters in word:
# #         print(letters)
# #         dubdub = letters * letters 
# #         return dubdub

# print(double_letters())









#     #  def test_double_letters():
# assert double_letters('hello') == 'hheelllloo'




# Count Letter
# Count the number of letter occurances in a string


# def count_letter():
#     word = input('Please enter a word: ')
#     letter = input('Please enter a letter to count: ')
#     return word.count(letter)

# print(count_letter())




# def test_count_letter():
#     assert count_letter('i', 'antidisestablishmentterianism') == 5
#     assert count_letter(
#         'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2



# Latest Letter
# Return the letter that appears the latest in the english alphabet.

# def latest_letter():
#     sorted = []
#     word = input('Please enter a word: ')
#     for letters in word:
#         sorted.append(letters)
#         sorted.sort()
#     return sorted.pop()
# print(latest_letter())

# def test_latest_letter():
#     return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# # Count Hi
# # Write a function that returns the number of occurances of 'hi' in a given string.

# def count_hi():
#     text_ls = []
#     text = input("Please enter some text here: ")
#     test_ls = text.split()
#     print(test_ls)
#     print(list(text))



#     # for pat in text:
#     #     text_ls.append()
#     #     text_ls.append(pat)
#     #     print(pat)
#     #     print(text_ls)
#     #     text_ls = text_ls.strip(',')
#     #     found = text_ls.find('hi')
#     #     f_count = found.count()
#     # return f_count

# print(count_hi())


# # def test_count_hi():
# #     assert count_hi('hihi') == 2
# #     assert count_hi('hello hi llama hill') == 2

# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).


test_con_1 = 'Hello World!'
test_con_2 = 'This is another example.'
import string
# print(string.ascii_lowercase)
def snake_case(text):
    text_ls = list(text)
    print(text_ls)
    for letter in text_ls:
        text_ls.append(letter)
        print(letter)


    # text = input('Please enter some words: ')
    # print(text)
    # text_ls = text.split()
    # print(text_ls)

print(snake_case(test_con_1))



def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'