
import requests
import string
text_ls =[]
response = requests.get('https://www.gutenberg.org/cache/epub/20203/pg20203.txt')
response.encoding = 'utf-8'
# print(response.text)
ben = response.text
# print(ben)
# with open('phonebook.txt', 'w',) as phone_book_file:
#     phone_book_file.write('hello world!')
bio_dict = {}
word_count = 0
with open('biowords.txt', 'w',  encoding='utf-8') as empty_file:
    # file = open('biowords.txt' "w")
    empty_file.write(ben)
with open('biowords.txt', 'r', encoding='utf-8') as new_book:
    text = new_book.read()
    print(text)
    text = text.strip(string.punctuation)
    text = text.lower()
    text_ls = text_ls.sort()
    text_ls = text.split(' ',-1)
    
for word in text_ls:
    if word in bio_dict:
       bio_dict = bio_dict[word]
    # text_ls = text_ls
    
    print(text_ls)