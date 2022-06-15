 
import requests
import string
punctuation = string.punctuation
print(punctuation)

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
# print(response.text)
book = response.text
# print(book)

# with open('the_raven.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# print(text)

word_dict_list = book.lower().strip(punctuation).split()
# new_dict = ' '.join(word_dict)
# split_dict = new_dict.split()
# word_dict = ' ' .join(word_dict)
# word_dicts = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
# words = list(word_dicts.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])
# print(type(word_dict))
# print(word_dicts)

# for word in word_dicts:
#     print(word_dicts[word])
#     if word == 'apples':
#         print('test')
#         word_dicts[word] += 15
# print(word_dicts)

# Creates a dict and then go through the list (word_dict_list) and count how many iterations of each word
word_dict = {}
for word in word_dict_list:
    if word not in word_dict:
        word_dict[word] = 1
    elif word in word_dict:
        word_dict[word] += 1
# print(word_dict)

# Shows the 10 most used words
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])