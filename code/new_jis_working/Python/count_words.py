#completed

with open('great_g.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = str(text).lower()

def stripped_text(string):
    special_character = ['`','~','!','@','#','$','%','^','&','*','(',')','-','+','=','{','[','}','}','|',':',';','<','>','?','.', ',','/','"',"'","_"]
   
    
    for x in string:
        for y in special_character:
            if x == y:
                string = string.replace(y, "")
    return string

text = stripped_text(text).split()

def word_counter(list_of_words):
    word_count = {}
    for word in list_of_words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count.update({word:1})
    return word_count

word_dict = word_counter(text)
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

