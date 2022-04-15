from audioop import reverse
import re

ghost_man = 'random txt\ghost.txt'

with open(ghost_man,'r', encoding='utf-8') as f:
    text = f.read()
    text = re.sub(r'[^\w\s\-]', '', text.replace('--',' ')
    .replace('-',' ').lower())
    text = text.split()
# print(text)


def text_sorted(text):
    answer = {}
    for item in range(len(text)):
        word = text[item]

        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1
    
    answer_list = list(answer.items())
    answer_list.sort(key=lambda item: item[1], reverse=True)
    return answer_list


def top_ten(lab):
    word = []
    for i in range(min(10, len(lab))):
        word.append(lab[i])
    return word
       




lab = text_sorted(text)
final_product = top_ten(lab)

print(final_product)