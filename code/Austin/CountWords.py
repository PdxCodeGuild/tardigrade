import string
import requests
import collections

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8'
separator = string.punctuation
book = response.text.lower()
punclessbook = book.translate(str.maketrans('','',string.punctuation))
spacelessbook = punclessbook.split()
top10wordsandoccurence = collections.Counter(spacelessbook).most_common(10)
print("These are the top 10 words and their counts:")
print(top10wordsandoccurence)

pairdict = collections.defaultdict(int)
duo = 2
for i in range(len(spacelessbook)-duo+1):
    key = tuple(spacelessbook[i:i+duo])
    pairdict[key] += 1

pairlist = collections.Counter(pairdict).most_common(10)
print("These are the top 10 word pairs and their counts:")
print(pairlist)