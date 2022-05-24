import string

with open('artofwar.txt', 'r', encoding='utf-8') as my_book:
    text = my_book.read()
    text = text.strip(string.punctuation).lower().split() #from the book, 
    # formatting it so i can then add it to my dictionar. so strip, lower case and add it to a string format
    
def book(pages):    
    word_dict = {}
    
    for item in range(len(pages)): #telling 'item to go through the book (text) when its called
        words = pages[item] # iterating through the book item by item and putting it as a varaible

        if words in word_dict:  #  seeing if word is in the dict. if not it will add it as a key and value of 1.
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    return word_dict
    # print(word_dict)

books = book(text) # calling book and adding text as a parameter. so it can pass the book through the call

words= list(books.items()) # formatting to a list
words.sort(key=lambda x: x[1], reverse=True) #sorting. telling that #1 should be last. or reverse the order
for idx in range(min(10, len(words))): # printing out the first ten in the dictionary. which in reverse means the top words
    print(words[idx])


# # text.replace(' ', '').strip('.').lower().replace('isa', 'IsA').replace('ex', 'Ex')
# #


