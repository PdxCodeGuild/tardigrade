with open('frank.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# print(text)

text = text.lower()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in text:
    if x in punc:
        text = text.replace(x, "")
        
list_text = text.split()
# print(list_text)

new_text = {}

for word in range(0, len(list_text)):
    single_word = list_text[word]
    
    if  single_word in new_text:
        new_text[single_word]+=1
    else:
        new_text[single_word]=1
# print(new_text)

words = list(new_text.items()) 
words.sort(key=lambda tup: tup[1], reverse=True)  
for i in range(min(10, len(words))):
    print(words[i])