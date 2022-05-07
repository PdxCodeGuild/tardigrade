
from hashlib import new
import requests
import string


response = requests.get('https://www.gutenberg.org/files/6695/6695-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8

text = response.text
text = text.lower()
punct = string.punctuation + '\”'
# print(punct)


#### loop over the text to remove punctuation
new_text = ""
for char in text:
    if char not in punct:
        new_text += char

#### loop over and make every word into a list at item

word_list = new_text.split()  ##### this just took my string with all the words in it "new_text" and split it into a list
                               #### Now I must loop throught the list and make a count for every word


word_dictionary = {}    ### this makes a dictionarty and adds the word count to it.
for word in word_list:
    if word not in word_dictionary:
        word_dictionary[word]= 1
    elif word in word_dictionary:
        word_dictionary[word] += 1

words = list(word_dictionary.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

