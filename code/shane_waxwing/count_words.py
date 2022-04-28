with open('frankenstein.txt', 'r') as book:
    contents = book.read()



    for letter in contents:
        if not letter.isalpha() and letter != " ":
            contents = contents.replace(letter, " ")
    
    new_words = contents.split()
    new_words.sort()
    

word_count = {}

for item in new_words:
    if item not in word_count:
        word_count.update({item : 1})
    elif item in new_words:
        word_count.update({item : word_count.get(item) +1})






words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])