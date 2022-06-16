## Eberhardt

## Version 1 - COMPLETE

## https://github.com/PdxCodeGuild/hydra/blob/master/1%20Python/labs/13%20Count%20Words.md

## WORKS - Yet manipulating the data from this import is complicated. Trying 'with open file' next. 
# import requests
# import string
# response = requests.get('https://www.gutenberg.org/files/62569/62569-0.txt')
# response.encoding = 'utf-8' 
# print(response.text)

from itertools import count
import string
string.punctuation

with open('the_monster_maker.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()

for char in string.punctuation:
    if char in text:
        text = text.replace(char, "")

word_list = []
word_list = text.split()

word_counter = {}

for item in word_list:
    if item not in word_counter:
        word_counter[item] = 1
    elif item in word_counter:
        word_counter[item] += 1

# print("Word counter: ", word_counter) # TEST STATEMENT

top_ten = sorted(word_counter.items(), key=lambda x:x[1])

rank = 1
counter = 0
index = -1
while counter <10:
    print(f"{rank}. ", top_ten[index])
    rank += 1
    counter += 1
    index -= 1
  
