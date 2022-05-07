import string

punct = string.punctuation

my_book = 'arabian_nights.txt'

with open(my_book, 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()

    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace(";", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace(":", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace("-", "")
    text = text.replace("_", "")
    text = text.replace("@", "")
    text = text.replace("*", "")
    text = text.replace("/", "")
    text = text.split()

# print(text)

word_dict = {}

for word in range(len(text)):
    single_word = text[word]
    if single_word in word_dict:
        word_dict[single_word] += 1
    else:
        word_dict[single_word] = 1

# print(word_dict)
# print(word_dict.items())

words = list(word_dict.items())  # .items() returns a list of tuples
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# print the top 10 words, or all of them, whichever is smaller
for i in range(min(10, len(words))):
    print(words[i])
