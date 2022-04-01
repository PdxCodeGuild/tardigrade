import random

adj_list=[]

name = input('please tell me your name: ')
noun = input('what do you like to do?: ')
adjective = input(f'describe in one word what you do when you play {noun}:  ')
adjective2= input ('pick another adjective: ')
adjective3= input ('pick another adjective: ')

adj_list.append(adjective)
adj_list.append(adjective2)
adj_list.append(adjective3)

# random.choice(adj_list)

results = (f' my name is {name}, i like to {random.choice(adj_list)} when playing {noun}. ')
print (results)